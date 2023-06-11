# Write a program that has a class called Fraction with attributes numerator and
# denominator.
# a.Write a method called getdata to enter the values of the attributes.
# b.Write a method show to print the fraction in simplified form.

class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def getdata(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))

    def show(self):
        
        gcd = self.gcd(self.numerator, self.denominator)
        simplified_numerator = self.numerator // gcd
        simplified_denominator = self.denominator // gcd

        print(f"The simplified fraction is: {simplified_numerator}/{simplified_denominator}")

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a


fraction = Fraction()


fraction.getdata()


fraction.show()
