def get_words_starting_with(alphabet, words):
    return [word for word in words if word[0].lower() == alphabet.lower()]

alphabet = input("Enter an alphabet: ")
words = ["apple", "banana", "cherry", "dog", "elephant"]

result = get_words_starting_with(alphabet, words)

if result:
    print("Words starting with '{}': {}".format(alphabet, result))
else:
    print("No words found starting with '{}'".format(alphabet))
