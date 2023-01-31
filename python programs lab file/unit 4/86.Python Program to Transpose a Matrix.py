def get_matrix(num_rows, num_cols):
    matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            element = int(input(f"Enter element ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def transpose(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed_matrix.append(transposed_row)
    return transposed_matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = get_matrix(rows, cols)

transposed = transpose(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed:
    print(row)
