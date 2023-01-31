from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

def max_num(x, y):
    return x if x > y else y

result = reduce(max_num, numbers)

print(result)
