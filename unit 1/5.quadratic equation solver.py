print("ax^2+bx+c=0","Compare your Equation ")
a=float(input("Enter cofficent of a: "))
b=float(input("Enter cofficent of b: "))
c=float(input("Enter cofficent c: "))
d=(b**2-4*a*c)
if d<0:
    print("Equation has Imaginary roots")
elif d==0:
    print("Equation has real and same roots")
elif d>0:
    print("Equation has real roots")
else:
    print("Enter correct values")

f=(-b+d)/(2*a)
g=(-b-d)/(2*a)
print("Roots of equation are:",f,"and",g)

