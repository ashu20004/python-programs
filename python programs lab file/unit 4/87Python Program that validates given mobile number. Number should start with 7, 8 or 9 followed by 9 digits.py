import re
def is_valid_mobile_number(number):
    pattern = r"^[7-9][0-9]{9}$"
    if re.match(pattern, number):
        return True
    return False

number = input("Enter mobile number: ")

if is_valid_mobile_number(number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
