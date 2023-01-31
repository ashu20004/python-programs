def leap(a):
    if a % 400 == 0 or (a % 4 == 0 and a% 100 != 0):
        return print(a,"is a leap year")
    else:
        return print(a,"is nopt a leap year")
a=int(input("Enter year: "))
leap(a)