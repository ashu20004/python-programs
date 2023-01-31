a=float(input("Enter First Digit: "))
b=float(input("Enter Second Digit: "))
if a%b==0:
    print(a,"is completely Divisible by",b)
elif a%b==1:
    print(a,"is not completely Divisible by",b)
else:
    print("Enter a valid input")
