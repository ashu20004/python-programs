filename=str(input("Enter file name: "))
file=open(filename,"r+")
word=0
lines=0
character=0
list1=[]
for line in file.readlines():
    lines+=1
    list1+=line.split(" ")
for ele in list1:
    word+=1
    for el in ele:
        character+=1

print("Word=",word,"\nLine=",lines,"\nCharacter=",character)       