# WAP to create a Complex class having real and imaginary as it attributes.
# Overload the +,-,/,* and += operators for objects of Complex class.

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        divisor = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / divisor
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / divisor
        return Complex(real, imaginary)

    def __iadd__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        return self
c1 = Complex(2, 3)
c2 = Complex(4, 5)

result = c1 + c2
print(result.real, "+", result.imaginary, "i")  

result += c1
print(result.real, "+", result.imaginary, "i")  