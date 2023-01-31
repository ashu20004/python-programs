def multiply_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        result.append(row)
    return result

rows1 = int(input("Enter number of rows for matrix 1: "))
columns1 = int(input("Enter number of columns for matrix 1: "))
rows2 = int(input("Enter number of rows for matrix 2: "))
columns2 = int(input("Enter number of columns for matrix 2: "))

if columns1 != rows2:
    print("Matrix multiplication not possible")
    exit()

mat1 = []
for i in range(rows1):
    row = list(map(int, input(f"Enter row {i + 1} elements for matrix 1 separated by space: ").split()))
    mat1.append(row)

mat2 = []
for i in range(rows2):
    row = list(map(int, input(f"Enter row {i + 1} elements for matrix 2 separated by space: ").split()))
    mat2.append(row)

result = multiply_matrices(mat1, mat2)

print("Result of matrix multiplication:")
for row in result:
    print(row)
