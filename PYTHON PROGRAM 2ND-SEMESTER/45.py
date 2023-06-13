# Write a NumPy program to compute the multiplication of two given matrixes.
import numpy as np
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[10, 11],
                    [12, 13],
                    [14, 15]])


result = np.matmul(matrix1, matrix2)


print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult of matrix multiplication:")
print(result)
