# Create a class called Complex. Write a menu driven program to read, display,
# add and subtract two complex numbers by creating corresponding instance
# methods.

class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def read(self):
        self.real = float(input("Enter the real part: "))
        self.imaginary = float(input("Enter the imaginary part: "))

    def display(self):
        print(f"{self.real} + {self.imaginary}i")

    def add(self, other_complex):
        real_sum = self.real + other_complex.real
        imaginary_sum = self.imaginary + other_complex.imaginary
        return Complex(real_sum, imaginary_sum)

    def subtract(self, other_complex):
        real_diff = self.real - other_complex.real
        imaginary_diff = self.imaginary - other_complex.imaginary
        return Complex(real_diff, imaginary_diff)



complex1 = Complex()
complex2 = Complex()


while True:
    print("\n--- Complex Number Operations ---")
    print("1. Read Complex Numbers")
    print("2. Display Complex Numbers")
    print("3. Add Complex Numbers")
    print("4. Subtract Complex Numbers")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("Enter Complex Number 1:")
        complex1.read()
        print("Enter Complex Number 2:")
        complex2.read()
    elif choice == 2:
        print("Complex Number 1:")
        complex1.display()
        print("Complex Number 2:")
        complex2.display()
    elif choice == 3:
        result = complex1.add(complex2)
        print("Sum of Complex Numbers:")
        result.display()
    elif choice == 4:
        result = complex1.subtract(complex2)
        print("Difference of Complex Numbers:")
        result.display()
    elif choice == 5:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a valid option (1-5).")
