numbers = list(map(int, input("Enter numbers separated by space: ").split()))

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)
