# number to binary
def number_to_binary():
    number = int(input("Enter a number: "))
    reuslt = bin(number)


def main():
    number = int(input("Enter a number: "))
    print(f"The binary representation of {number} is {str(bin(number))[2:]}")


main()
