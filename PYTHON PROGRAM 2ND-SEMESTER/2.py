#Write a program to implement default constructor, parameterized constructor, and destructor

class default:
    def __init__(self):
        return print("Default constructor")
    def __del__(self):
        return print("destructor called")
    
class default1:
    def __init__(self,name):
        return print(f"{name} called parameterized constructor")
    def __del__(self):
        return print("destructor called")
    

ashu=default()
ashu1=default1("ashu")

del ashu
del ashu1
