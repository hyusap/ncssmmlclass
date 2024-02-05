def is_over_21(number):
    return 0 if number > 21 else number


def main():
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))

    number_one = is_over_21(number_one)
    number_two = is_over_21(number_two)

    print(number_one if number_one > number_two else number_two)


if __name__ == "__main__":
    main()
