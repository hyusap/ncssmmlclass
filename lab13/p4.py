import functions

number_of_numbers = int(input("Enter the number of numbers: "))
numbers = []
for i in range(number_of_numbers):
    number = int(input("Enter a number: "))
    numbers.append(number)
value = int(input("Enter a value: "))
print(functions.sum_of_numbers_divisible_by_value(numbers, value))
