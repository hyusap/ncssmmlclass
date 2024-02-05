# Ask the user for two integers greater than 0, and print whichever is nearest to 21 without going over.
# Return 0 if they both go over.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > 21 and number2 > 21:
    print(0)
elif number1 > 21:
    print(number2)
elif number2 > 21:
    print(number1)
else:
    print(number1 if 21 - number1 < 21 - number2 else number2)

# Number of code paths: 5
