numbers = list(map(int, input("Enter numbers separated by space: ").split()))

min_num = min(numbers)
max_num = max(numbers)
avg = sum(numbers) / len(numbers)

print("Minimum:", min_num)
print("Maximum:", max_num)
print("Average:", avg)
