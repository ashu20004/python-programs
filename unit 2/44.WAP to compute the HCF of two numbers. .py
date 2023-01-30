a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    a,b=a,b
        
else:
    a,b=b,a
for i in range(1, a+1):
    if((a % i == 0) and (b % i == 0)):
        hcf = i

print(hcf)       