def invert_dict(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    return inverted_dict

dictionary = eval(input("Enter a dictionary: "))

inverted_dict = invert_dict(dictionary)

print("Inverted dictionary:", inverted_dict)
