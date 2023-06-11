# Create a class called String that stores a string and all its status details such as
# number of uppercase letters, lowercase letters, vowels ,consonants and space
# in instance variables.
# a.Write methods named as count_uppercase, count_lowercase, count_vowels, count_consonants and count_space to count corresponding
# values.
# b.
# Write a method called display to print string along with all the values
# computed by methods in (a).

class String:
    def __init__(self, string):
        self.string = string
        self.uppercase = 0
        self.lowercase = 0
        self.vowels = 0
        self.consonants = 0
        self.space = 0

    def count_uppercase(self):
        for i in self.string:
            if i.isupper():
                self.uppercase += 1

    def count_lowercase(self):
        for i in self.string:
            if i.islower():
                self.lowercase += 1

    def count_vowels(self):
        for i in self.string:
            if i in "aeiouAEIOU":
                self.vowels += 1

    def count_consonants(self):
        for i in self.string:
            if i not in "aeiouAEIOU":
                self.consonants += 1

    def count_space(self):
        for i in self.string:
            if i == " ":
                self.space += 1

    def display(self):
        print("String:", self.string)
        print("Uppercase:", self.uppercase)
        print("Lowercase:", self.lowercase)
        print("Vowels:", self.vowels)
        print("Consonants:", self.consonants)
        print("Space:", self.space)


string1 = String("Hello World")
string1.count_uppercase()
string1.count_lowercase()
string1.count_vowels()
string1.count_consonants()
string1.count_space()
string1.display()

