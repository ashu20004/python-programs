a=int(input("Enter First Digit: "))
b=int(input("Enter Second Digit: "))
c=int(input("Enter Third Digit: "))

if a<b:
    if a<c:
        print(a,"First Digit is Smallest")
    elif c<a:
        print(c,"Third Digit is Smallest")
    else:
        print("All are Smae")
elif b<a:
    if b<c:
        print("Second Digit is Smallest")
    elif c<b:
        print("Third Digit is Smallest")
    else:
        print("All Are same")

else:
    print("Enter a valid input")
