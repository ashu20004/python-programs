n=int(input("Enter a number: "))
if n==2 or n==3 or n==5 or n==7:
    print(n,"is a prime number")
elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
    