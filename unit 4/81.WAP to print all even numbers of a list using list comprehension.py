numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers:", even_numbers)
