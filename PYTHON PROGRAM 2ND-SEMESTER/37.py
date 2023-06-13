# Write a program to create a generator to print the Fibonacci number.

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for i in fib():
    print(i)
    