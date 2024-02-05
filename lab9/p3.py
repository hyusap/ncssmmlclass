a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


def round10(n):
    if n % 10 >= 5:
        return n + 10 - n % 10
    else:
        return n - n % 10


print(round10(a) + round10(b) + round10(c))


# Number of code paths: 2 but its called 3 times so i guess 6?
