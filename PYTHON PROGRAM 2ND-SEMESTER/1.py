# Write a program illustrating class definition and accessing class members. 
class csee:
    def student(self,name,marks):
        self.name=name
        self.mark=marks
        return f"{self.name}"


    def Mark(self):
        
        return f"{self.name} obtained {self.mark} marks"
    


ashu=csee()

ashu.student('ashish',98)

print(ashu.Mark())