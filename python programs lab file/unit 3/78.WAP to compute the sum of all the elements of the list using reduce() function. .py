from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

def add(x, y):
    return x + y

result = reduce(add, numbers)

print(result)
