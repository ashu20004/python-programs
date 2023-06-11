# Create a class named as Student to store the name and marks in three
# subjects. Use List to store the marks.
# a. Write an instance method called compute to compute total marks and
# average marks of a student.
# b. Write a method called display to display student information

class Student:
    

    def __init__(self,name,maths,science,it):
        self.name=name
        self.maths=maths
        self.science=science
        self.it=it
        self.sumi=maths+science+it
        self.average=self.sumi/3
        self.name=[self.maths,self.science,self.it]
        return  
    
    def compute(self):
        return f"Total marks of {self.name} ={self.sumi} and Average={self.average}"

    def display(self):
        return f"{self.name} maths={self.maths} \nscience={self.science} \nit={self.it}"
    

ashu=Student("Ashish",50,50,80)

print(ashu.compute())
print(ashu.display())