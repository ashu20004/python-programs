# Write a program that creates an iterator to print squares of numbers.

class Squares:  
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n**2
            self.n += 1
            return result
        else:
            raise StopIteration
        
squares = Squares(5)
for i in squares:
    print(i)
    