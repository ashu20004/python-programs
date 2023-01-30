import math
n=int(input("Enter a number: "))
x=int(input("Enter value of x: "))
sum=1
for i in range(1,n+1):
    sum+=(x**i)/math.factorial(i)
print(sum)