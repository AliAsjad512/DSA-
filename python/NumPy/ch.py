import numpy as np

# 1. Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# 2. Perform basic operations
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)

# 3. Create a 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Matrix:\n", matrix)

# 4. Access elements
print("Element at row 1, column 2:", matrix[1, 2])

# 5. Slicing
print("First two rows:\n", matrix[:2])
print("Last column:", matrix[:, -1])

# 6. Mathematical operations
print("Sum of all elements:", np.sum(matrix))
print("Mean of all elements:", np.mean(matrix))
print("Transpose of matrix:\n", np.transpose(matrix))

import numpy as np

# Create the array
arr = np.arange(10, 51)
print("Original array:", arr)

# Find numbers divisible by 7
div_by_7 = arr[arr % 7 == 0]
print("Numbers divisible by 7:", div_by_7)

import numpy as np

# Create 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate determinant
det = np.linalg.det(matrix)
print("Determinant:", det)


import numpy as np

# Generate 5x5 random matrix
matrix = np.random.rand(5, 5)
print("Random Matrix:\n", matrix)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)
print("Row-wise sum:", row_sum)

