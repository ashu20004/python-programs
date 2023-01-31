a=float(input("Enter First side: "))
b=float(input("Enter Second side: "))
c=float(input("Enter Third side: "))
s=(a+b+c)/2
print("Value of s:",s)
print("Area of Triangle:",(s*(s-a)*(s-b)*(s-c))**0.5)
