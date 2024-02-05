import functions


def main():
    word = input("Enter a word: ")
    letter = input("Enter a letter: ")
    count = functions.count_letters_in_word(word, letter)
    print(f"The letter {letter} appears {count} times in {word}.")


if __name__ == "__main__":
    main()
