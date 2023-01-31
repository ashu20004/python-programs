def sum_of_n(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_n(n-1)
n=int(input("Enter a number: "))
print(sum_of_n(n))