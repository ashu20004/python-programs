filename =str( input("Enter filename: "))

with open(filename,'r') as file:
    for line in file.readlines():
        print(line)
    
file.close()
