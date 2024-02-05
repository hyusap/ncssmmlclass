import functions


def main():
    word = input("Enter a word: ")
    code = input("Enter a code: ")
    count = functions.find_word_in_string(word, code)
    print(f"The code {code} appears {count} time{"s" if count != 1 else "" } in {word}.")


if __name__ == "__main__":
    main()
