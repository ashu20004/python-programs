# Write a program to overload inoperator.

class MyClass:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


my_list = [1, 2, 3, 4, 5]
my_class = MyClass(my_list)
print(3 in my_class)  
print(6 in my_class)  
