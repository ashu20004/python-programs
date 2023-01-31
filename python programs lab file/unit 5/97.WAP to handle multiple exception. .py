try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Second number cannot be zero.")
except ValueError:
    print("Invalid input. Both numbers should be integers.")
except Exception as e:
    print("Some error occurred:", e)
