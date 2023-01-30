def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

def lcm(a, b):
    return (a * b) // hcf(a, b)
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(hcf(a,b)) 
print(lcm(a,b)) 
