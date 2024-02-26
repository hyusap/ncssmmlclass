import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openai import OpenAI
import base64
import io

client = OpenAI()

dfs = [pd.read_csv("data1.csv"), pd.read_csv("data2.csv"), pd.read_csv("data3.csv")]


def get_analysis_from_image(image_base64):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyse this graph and create an insight for the relationship between the two variables in 2 sentences.",
                    },
                    {
                        "type": "image",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content


for df in dfs:
    x_column = df.columns[0]
    x = df[x_column]
    y_column = df.columns[1]
    y = df[y_column]

    x_bar = np.mean(x)
    y_bar = np.mean(y)

    x_diff = x - x_bar
    y_diff = y - y_bar

    m = np.sum(x_diff * y_diff) / np.sum(x_diff**2)
    b = y_bar - m * x_bar

    y_pred = m * x + b
    mse = np.mean((y - y_pred) ** 2)

    print(f"y = {m:.2f}x + {b:.2f}")
    print(f"mse = {mse:.2f}")

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{x_column} vs {y_column} (m={m:.2f}, b={b:.2f}, mse={mse:.2f})")

    plt.scatter(x, y)
    plt.plot(x, m * x + b, color="red")

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format="jpg")
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

    # print(my_base64_jpgData)

    analysis = get_analysis_from_image(my_base64_jpgData)
    print(analysis)

    plt.show()


"""
loose correlation between the two variables, with a positive slope. The relationship is not very strong, but it is present. potenially other factors influencing the relationship between the two variables.

tight correlation between the variables with a negative slope: The scatter plot shows a negative linear relationship between hours studied and time taken, indicating that as study time increases, the time taken to complete a task decreases. The slope of the line (m = -6.26) suggests a moderately strong inverse correlation between the two variables.

The graph displays a positive linear relationship between the amount of fertilizer used and crop yield, indicating that as the amount of fertilizer increases, the crop yield tends to increase as well. The parameters given (m=2.02, b=20.82) suggest that for every kilogram of fertilizer used, the crop yield increases by approximately 2.02 kilograms, assuming the relationship is causal and other factors are held constant.
"""
