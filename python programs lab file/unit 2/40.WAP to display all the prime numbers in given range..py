a=int(input("Enter a number: "))
for n in range(a+1):
    if n==2 or n==3 or n==5 or n==7:
        print(n,end=",")
    elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
        pass
    else:
        print(n,end=",")
    