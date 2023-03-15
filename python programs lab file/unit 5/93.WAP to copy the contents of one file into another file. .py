filename=str(input("Enter name of file: "))
file=open(filename,"r+")
file1=open("93 sample file.txt","a+" )
for line in file.readlines():
    file1.writelines(line)

file1.close()
file.close()