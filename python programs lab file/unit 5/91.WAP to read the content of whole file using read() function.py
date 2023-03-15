a=str(input("Enter file name: "))

file=open('{}'.format(a),'r')

print(file.read())
file.close()
