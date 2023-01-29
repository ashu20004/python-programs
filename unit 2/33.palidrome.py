num=int(input("Enter a number: "))
new=num
number=0
while num>0:
    rem=num%10
    number=(number*10)+rem
    num//=10
if number==new:
    print(number,"Number is a palidrome number")
else:
    print(number,"Number is not a palidrome number")