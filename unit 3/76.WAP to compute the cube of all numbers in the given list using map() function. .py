numbers = list(map(int, input("Enter numbers separated by space: ").split()))

def cube(x):
    return x**3

result = list(map(cube, numbers))

print(result)