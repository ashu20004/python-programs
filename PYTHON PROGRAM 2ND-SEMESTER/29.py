# Write a program to inspect the object using type() ,id(), isinstance(), issubclass()
# and callable() built-in function.

class MyClass:
    def __init__(self):
        self.data = 10

    def my_method(self):
        print("Hello, World!")
obj = MyClass()

print("Type of obj:", type(obj))


print("ID of obj:", id(obj))
print("Is obj an instance of MyClass?", isinstance(obj, MyClass))

print("Is MyClass a subclass of object?", issubclass(MyClass, object))


print("Is my_method callable?", callable(obj.my_method))
print("Is data callable?", callable(obj.data))
