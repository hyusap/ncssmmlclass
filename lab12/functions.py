def reverse_string_with_while_loop(s):
    result = ""
    index = len(s) - 1
    while index >= 0:
        result += s[index]
        index -= 1
    return result


def count_letters_in_word(word, letter):
    count = 0
    index = 0
    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1
    return count


def find_word_in_string(s, word):
    index = 0
    count = 0
    while index < len(s):
        if s[index : index + len(word)].lower() == word:
            count += 1
        index += 1
    return count


if __name__ == "__main__":
    assert reverse_string_with_while_loop("hello") == "olleh"
    assert reverse_string_with_while_loop("world") == "dlrow"

    assert count_letters_in_word("hello", "l") == 2
    assert count_letters_in_word("world", "o") == 1
    assert count_letters_in_word("world", "z") == 0

    assert find_word_in_string("hello world", "hello") == 1
    assert find_word_in_string("hello world hello", "hello") == 2
    assert find_word_in_string("hello world hello", "world") == 1
    assert find_word_in_string("Hello world hello", "hello") == 2
    assert find_word_in_string("hello world hello", "z") == 0
    print("All tests passed!")
