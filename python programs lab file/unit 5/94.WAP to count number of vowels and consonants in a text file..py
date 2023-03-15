filename=str(input("Enter file name: "))
file=open(filename,"r+")
vowel=0
consonant=0
for line in file:
    for el in line:
        if (el=="a") or (el=="i") or (el=="o") or (el=="e") or (el=="u"):
            vowel+=1

        elif el==" ":
            pass
        else:
            consonant+=1
            
        

print("vowel=",vowel,"\nconsonat=",consonant)