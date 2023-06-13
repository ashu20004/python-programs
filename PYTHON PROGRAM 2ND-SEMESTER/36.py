# Write a program to create a generator that starts counting from 0 and raise an
# exception when counter is equal to 10.

def gen():
    n=0
    while n<10:
        yield n
        n+=1
        if n==10:
            raise StopIteration
for i in gen():
    print(i)