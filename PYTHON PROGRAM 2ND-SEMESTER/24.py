# Write a program to demonstrate hybrid inheritance and show MRO for each
# class.
class A:
    def __init__(self):
        print("Initializing class A")

    def method_A(self):
        print("Method A from class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing class B")

    def method_B(self):
        print("Method B from class B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing class C")

    def method_C(self):
        print("Method C from class C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Initializing class D")

    def method_D(self):
        print("Method D from class D")

d = D()

print("\nMethod Resolution Order (MRO) for class D:", D.__mro__)
print("Method Resolution Order (MRO) for class B:", B.__mro__)
print("Method Resolution Order (MRO) for class C:", C.__mro__)
print("Method Resolution Order (MRO) for class A:", A.__mro__)


d.method_A()
d.method_B()
d.method_C()
d.method_D()
