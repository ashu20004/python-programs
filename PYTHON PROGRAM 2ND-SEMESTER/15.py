# Write a program to illustrate the use of following built-in methods:
# a. hasattr(obj,attr)
# b. getattr(object, attribute_name [, default])
# c. setattr(object, name, value)
# d. delattr(class_name, name)

class MyClass:
    def __init__(self, value):
        self.value = value



my_obj = MyClass(42)


if hasattr(my_obj, 'value'):
    print("The object has an attribute called 'value'.")


value = getattr(my_obj, 'value')
print("The value of 'value' attribute:", value)

setattr(my_obj, 'name', 'John')
print("The value of 'name' attribute:", my_obj.name)


delattr(MyClass, 'value')


