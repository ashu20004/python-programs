n = int(input("Enter a number: "))
for i in range(1, n + 1):
    num = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** num
        temp //= 10
    if sum == i:
        print(i)
