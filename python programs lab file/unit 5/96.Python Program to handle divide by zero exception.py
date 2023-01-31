try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
