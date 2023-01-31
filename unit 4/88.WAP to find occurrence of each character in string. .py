def char_occurrence(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

string = input("Enter a string: ")

char_dict = char_occurrence(string)

print("Occurrence of each character in the string:")
for char, count in char_dict.items():
    print(f"{char}: {count}")
