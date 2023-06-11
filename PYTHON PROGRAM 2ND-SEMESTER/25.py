# Write a program to overload + operator to multiply to fraction object of fraction
# class which contain two instance variable numerator and denominator. Also,
# define the instance method simplify() to simplify the fraction objects.

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result
fraction1 = Fraction(2, 3)
fraction2 = Fraction(3, 4)

result = fraction1 + fraction2


print("Result:", result)
