def nCr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter n: "))
r=int(input("Enter r: "))
print(nCr(n,r))