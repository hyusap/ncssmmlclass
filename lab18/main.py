dictionary = {}
with open("lab18/dict.txt", "r") as file:
    for line in file:
        word, _, definition = line.split(",")
        dictionary[word] = definition.strip()

input_word = input("Enter a word: ")
while input_word != "exit":
    if input_word in dictionary:
        print(dictionary[input_word])
    else:
        print("Word not found")
    input_word = input("Enter a word: ")
