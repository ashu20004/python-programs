def large(a,b,c):
    if a>b:
        if a>c:
            print(a,"First Digit Is gratest")
        elif a<c:
            print(c,"Third Digit is gratest")
        else:
            print("All are same")
    elif b>a:
        if b>c:
            print(b,"Second Digit is gratest")
        elif b<c:
            print(c,"Third Digit is gratest")
        else :
            print("All are same")
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
large(a,b,c)