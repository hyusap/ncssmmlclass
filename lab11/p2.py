def new_value(number):
    if number in [13, 14, 17, 18, 19]:
        return 0
    return number


def main():
    num1 = new_value(int(input("Enter the first number: ")))
    num2 = new_value(int(input("Enter the second number: ")))
    num3 = new_value(int(input("Enter the third number: ")))
    print(f"The sum of the numbers is {num1 + num2 + num3}")


if __name__ == "__main__":
    main()
