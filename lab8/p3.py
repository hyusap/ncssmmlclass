skipped_nums = [13, 14, 17, 16, 19]
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

num1 = num1 if num1 not in skipped_nums else 0
num2 = num2 if num2 not in skipped_nums else 0
num3 = num3 if num3 not in skipped_nums else 0

print(f"The sum of the numbers is {num1 + num2 + num3}")
