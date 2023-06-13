# Write a program that convert a list of temperatures in Celsius into Fahrenheit
# using map() function.

def convert(c):
    return (c*9/5)+32

celsius=[10,20,30,40,50]
fahrenheit=list(map(convert,celsius))
print(fahrenheit)   
