# Write a NumPy program to create an array of (3, 4) shape, multiply every
# element value by 3 and display the new array.

import numpy as np

# Create the original array
original_array = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])

new_array = original_array * 3

print("Original Array:")
print(original_array)
print("\nNew Array (After multiplication):")
print(new_array)
