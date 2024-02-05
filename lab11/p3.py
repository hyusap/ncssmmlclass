def round(num):
    last_digit = num % 10
    if last_digit < 5:
        return num - last_digit
    else:
        return num + (10 - last_digit)


def main():
    num1 = round(int(input("Enter the first number: ")))
    num2 = round(int(input("Enter the second number: ")))
    num3 = round(int(input("Enter the third number: ")))
    print(f"The sum of the numbers is {num1 + num2 + num3}")


if __name__ == "__main__":
    main()
