a=int(input("Enter longest side:"))
b=int(input("Enter shorte side:"))
c=int(input("Enter Shortest side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Scalene Triangle={}".format(area))

