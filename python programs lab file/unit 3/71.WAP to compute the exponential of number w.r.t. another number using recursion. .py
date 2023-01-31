def exponent(base, power):
    if power == 0:
        return 1
    else:
        return base * exponent(base, power-1)
a=int(input("Enter base: "))
b=int(input("Enter power: "))
print(exponent(a,b)) 


