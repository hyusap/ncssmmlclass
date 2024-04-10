starting_number = 1 / 3
common_ratio = 1 / 2
limit = 30
threshold = 1e-6
result = starting_number
number_of_terms = 0
for i in range(0, limit):
    number_of_terms += 1
    result += starting_number * common_ratio ** (i + 1)
    if starting_number * common_ratio**i < threshold:
        break
print(f"{number_of_terms=}, {result=}")
