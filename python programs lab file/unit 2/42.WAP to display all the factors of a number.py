num=int(input("Enter a number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
        print(i,end=", ")
        count+=1
print(count)