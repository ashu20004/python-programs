a=int(input("Enter Year: "))
if a%4==0 and a%400==0:
    if a%100==0:
        print(a,"Is a Normal year")
    else:
        print(a,"is a Leap Year")
else:
    print(a,"Is a Normal YEAR")
