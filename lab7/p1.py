name = input("Enter your name: ")
number_of_apples = int(input("Enter the number of apples: "))
number_of_pears = int(input("Enter the number of pears: "))
number_of_peaches = int(input("Enter the number of peaches: "))
total = (
    number_of_apples * 0.5
    + number_of_pears * 0.75
    + number_of_peaches * 0.9
    + (5 if name == "Darth" else 0)
)
print(f"Total cost for {name} is ${total:.2f}")
