def all_positive_even_ints_backwards(n):
    value = n
    while value > 0:
        if value % 2 == 0:
            print(value)
        value -= 1


def powers_of_two_up_to(n):
    value = 2
    while value < n:
        print(value)
        value *= 2


def bottles_of_beer(n):
    value = n
    while value > 0:
        print(f"{value} bottles of beer on the wall, {value} bottles of beer.")
        value -= 1
        print(f"Take one down, pass it around, {value} bottles of beer on the wall.")


def sum_of_numbers_divisible_by_value(n, value):
    total = 0
    for i in n:
        if i % value == 0:
            total += i
    return total


if __name__ == "__main__":
    all_positive_even_ints_backwards(10)
    all_positive_even_ints_backwards(5)
    bottles_of_beer(5)
