math=float(input("Enter Maths marks: "))
phy=float(input("Enter Physics marks: "))
chm=float(input("Enter Chemistry marks: "))
eng=float(input("Enter English marks: "))
it=float(input("Enter IT marks: "))
tm=(math+phy+chm+eng+it)
print("Total marks obtained out of 500:",tm)
per=(tm*100)/500
print("Obtained percentage:",per)
if per==100 and per>=90:
    print("Grade : A")
elif per<90 and per>=80:
    print("Grade : B")
elif per<80 and per>=60:
    print("Grade : C")
elif per<60 and per>=50:
    print("Grade : D")
elif per<50 and per>=40:
    print("Grade : E")
elif per<40:
    print("Grade : F")
