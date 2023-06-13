# Write a program using reduce() function to calculate the sum of first 10 natural
# numbers

from functools import reduce

def sum_(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum1 = reduce(sum_, numbers)
print(sum1)
