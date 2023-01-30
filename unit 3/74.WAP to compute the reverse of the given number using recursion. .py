def reverse(n):
    if n == 0:
        return 0
    else:
        return int(str(n % 10) + str(reverse(n // 10)))
n=int(input("Enter a number: "))
print(reverse(n)) 
