list_of_string_numbers = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
list_of_numbers = list(map(int, list_of_string_numbers))
print(list_of_numbers)


list_of_numbers = [-2, -1, 0, 1, 2]
list_of_abs_numbers = list(map(abs, list_of_numbers))

print(list_of_abs_numbers)

list_of_numbers = [-2, -1, 0, 1, 2]
list_of_float_numbers = list(map(float, list_of_numbers))

print(list_of_float_numbers)

list_of_names = ["Scooby", "Shaggy", "Velma", "Fred", "Daphne"]
list_of_lens = list(map(len, list_of_names))

print(list_of_lens)

numbers1 = [4, 9, 22, 16, 5, 10, 13]
numbers2 = [24, 19, 122, 6, 25, 21, 231]
list_of_diff = list(map(lambda x, y: x - y, numbers1, numbers2))

print(list_of_diff)


numbers1 = [4, 9, 222, 16, 5, 10, 13]
numbers2 = [24, 9, 122, 6, 25, 21, 231]

greater_than = list(map(lambda x, y: x >= y, numbers1, numbers2))

print(greater_than)


names = ["Scooby", "Shaggy", "Velma", "Fred", "Daphne"]
numbers2 = [10, 3, 4, 6, -1]

capped_lengths = list(map(lambda x, y: x[:y], names, numbers2))

print(capped_lengths)


list_of_numbers = [
    4,
    8,
    6,
    5,
    3,
    2,
    8,
    9,
    2,
    204,
    101,
    130,
    150,
    200,
    250,
    300,
    350,
    400,
    450,
    500,
]
list_less_than_102 = list(filter(lambda x: x < 102, list_of_numbers))

print(list_less_than_102)

list_of_strings = [
    "Hello world",
    "Hey there",
    "Hey world",
    "Hello there",
    "Hello world",
]
strings_starting_with_hey = list(filter(lambda x: x.startswith("Hey"), list_of_strings))

print(strings_starting_with_hey)
