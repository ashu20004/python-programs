a=input("Enter a charater or a number only: ")
b=a.lower()
if (b=="a"or b=="i" or b=="e" or b=="o" or b=="u"):
    print(a, "is a vowel")

elif (b=="b"or b=="c"or b=="d"or b=="f"or b=="g"or b=="h"or b=="j"or b=="k"or b=="l"or b=="m"or b=="n"or
      b=="p"or b=="q"or b=="r"or b=="s"or b=="t"or b=="v"or b=="w"or b=="x"or b=="y"or b=="z" ):
    print(a,"is a consonant")
    

if a.isdigit():
    c=int(a)
    if c%2==0 or c%2==1:

        print(a,"is a digit")
    

