def swap_globals():
    global x, y
    x, y = y, x

x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
swap_globals()
print(x,y)
