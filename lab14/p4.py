letters = "abcdefghijklmnopqrstuvwxyz"


def letter_to_ascii(letter):
    return ord(letter)


def main():
    for letter in letters:
        print(f"{letter} {letter_to_ascii(letter)}")


main()
