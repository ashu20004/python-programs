# WAP to inspect the program code using the functions of inspect module.

import inspect

def inspect_code(obj):
    source_code = inspect.getsource(obj)
    print("Source code:")
    print(source_code)

def inspect_attributes(obj):
    attributes = inspect.getmembers(obj)
    print("Attributes:")
    for attr_name, attr_value in attributes:
        print(f"{attr_name}: {attr_value}")

def inspect_arguments(obj):
    signature = inspect.signature(obj)
    parameters = signature.parameters
    print("Arguments:")
    for param_name, param in parameters.items():
        print(f"{param_name}: {param.default}")

# Example usage
def my_function(a, b):
    return a + b

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

inspect_code(my_function)
inspect_attributes(MyClass("Ashu"))
inspect_arguments(my_function)
inspect_arguments(MyClass("ashu").greet)
