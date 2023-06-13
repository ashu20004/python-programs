# Write a program to create a new list containing the first letters of every
# element in an already existing list.

class List:
    def __init__(self, items):
        self.newlist=[]
        for i in items:
            self.newlist.append(i[0])
             
    def dispaly(self):
        return self.newlist
item=["apple","ball","cat","dog"]    
a=List(item)
print(a.dispaly())


    