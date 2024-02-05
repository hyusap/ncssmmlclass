a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
small = min(a, b, c)
large = max(a, b, c)
medium = a + b + c - small - large

if medium - small == large - medium:
    print("Evenly Spaced")
else:
    print("Not Evenly Spaced")


# Number of code paths: 2
