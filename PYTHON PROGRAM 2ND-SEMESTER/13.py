# Write a Program to illustrate the use of __str__(), __repr__(), __new__,
# __doc__, __dict__, __name__ and __bases__ methods.

class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Instance of MyClass with name: {self.name}"

    def __repr__(self):
        return f"MyClass({self.name})"

    def __new__(cls, name):
        print("Creating a new instance using __new__ method")
        return super().__new__(cls)

    def __doc__(self):
        return "This is the documentation for MyClass"

    def __dict__(self):
        return {"name": self.name}

    @property
    def __name__(self):
        return "MyClass"

    def __bases__(self):
        return (object,)



my_obj = MyClass("Example")

print(str(my_obj))

print(repr(my_obj))

print(my_obj)

print(my_obj.__doc__())

print(my_obj.__dict__())

print(my_obj.__name__)

print(my_obj.__bases__())
