numbers = list(map(int, input("Enter numbers separated by space: ").split()))

def is_odd(x):
    return x % 2 != 0

result = list(filter(is_odd, numbers))

print(result)
