rows = 5
k = 2 * rows - 2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(i+1,0,-1):
        print("*", end=" ")
    print("")