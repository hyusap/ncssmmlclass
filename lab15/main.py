def average(lst):
    return sum(lst) / len(lst)


def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_input():
    numbers = []
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        numbers.append(int(number))
    return numbers


def main():
    name = input("Enter your name: ")
    numbers = get_input()
    avg = average(numbers)
    print(f"The average is {avg} and the letter grade is {letter_grade(avg)}.")


if __name__ == "__main__":
    main()
