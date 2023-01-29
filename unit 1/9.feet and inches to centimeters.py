a=str(input("Enter f for feet and in for Inches: "))
b=float(input("Enter Height: "))
if a=="f":
    print(b*12*2.54,"centimeters")

elif a=="in":
    print(b*2.54,"centimeters")
else:
    print("Please enter valid input")
