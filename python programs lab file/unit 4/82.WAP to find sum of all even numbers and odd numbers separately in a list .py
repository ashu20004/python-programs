numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_sum = sum([num for num in numbers if num % 2 == 0])
odd_sum = sum([num for num in numbers if num % 2 != 0])

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
