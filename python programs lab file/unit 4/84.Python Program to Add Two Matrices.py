def add_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

mat1 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split()))
    mat1.append(row)

mat2 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split()))
    mat2.append(row)

result = add_matrices(mat1, mat2)

print("Result of matrix addition:")
for row in result:
    print(row)
