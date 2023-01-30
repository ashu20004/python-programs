n=int(input("Enter a number: "))
sum_of_odd=0
sum_of_even=0
for i in range(n+1):
    if i%2==0:
        sum_of_even+=i
    else:
        sum_of_odd+=i
print("Sum of odd number:",sum_of_odd,"\nSum of Even number:",sum_of_even)