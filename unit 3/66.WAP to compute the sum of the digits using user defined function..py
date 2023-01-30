def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])
n=int(input("Enter a number: "))
print(sum_of_digits(n)) # 15
