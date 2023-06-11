# Write a program that has a class Numbers with a list as an instance variable.
# a.Write a method called insert_element that takes values from user.
# b.Write a class method called find_max to find and print largest value in the
# list.

class Numbers:
    def __init__(self):
        self.number_list = []

    def insert_element(self):
        while True:
            value = input("Enter a number (or 'q' to quit): ")
            if value == 'q':
                break
            try:
                number = int(value)
                self.number_list.append(number)
            except ValueError:
                print("Invalid input. Please enter a number.")

    @classmethod
    def find_max(cls,self):
        if not self.number_list:
            print("The list is empty.")
        else:
            max_number = max(self.number_list)
            print("The largest number in the list is:", max_number)



numbers = Numbers()


numbers.insert_element()


Numbers.find_max(numbers)
