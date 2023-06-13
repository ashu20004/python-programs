# Write a program that create a custom iterator to create even numbers.

class Even:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration
        
even = Even(10)
for i in even:  
    print(i)    
    