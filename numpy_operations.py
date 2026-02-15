"""
NumPy Operations Demonstration
Author: Manoj
Description: Covers array creation, math operations, broadcasting,
statistics, comparison with lists, random data, optimization,
and structure visualization.
"""

import numpy as np
import time

print("===== NUMPY OPERATIONS DEMO =====\n")

# -------------------------------------------------------
# 1. Create Arrays of Different Dimensions
# -------------------------------------------------------

print("1️⃣ Creating Arrays\n")

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr3)

print("Shape of 3D Array:", arr3.shape)
print("Dimensions:", arr3.ndim)
print("-" * 50)


# -------------------------------------------------------
# 2. Mathematical Operations
# -------------------------------------------------------

print("2️⃣ Mathematical Operations\n")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)

print("-" * 50)


# -------------------------------------------------------
# 3. Broadcasting
# -------------------------------------------------------

print("3️⃣ Broadcasting\n")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Original Matrix:\n", matrix)

# Add scalar
print("\nMatrix + 10:\n", matrix + 10)

# Add 1D array to 2D array
row = np.array([1, 1, 1])
print("\nMatrix + Row Vector:\n", matrix + row)

print("-" * 50)


# -------------------------------------------------------
# 4. Statistical Functions
# -------------------------------------------------------

print("4️⃣ Statistical Functions\n")

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

print("-" * 50)


# -------------------------------------------------------
# 5. NumPy vs Python List Performance
# -------------------------------------------------------

print("5️⃣ NumPy vs Python List Performance\n")

size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
py_result = [x * 2 for x in py_list]
print("Python list time:", time.time() - start)

# NumPy array
np_array = np.arange(size)
start = time.time()
np_result = np_array * 2
print("NumPy array time:", time.time() - start)

print("-" * 50)


# -------------------------------------------------------
# 6. Generate Random Data
# -------------------------------------------------------

print("6️⃣ Random Data Generation\n")

print("Random integers:\n", np.random.randint(1, 100, size=(3, 3)))
print("\nRandom floats:\n", np.random.rand(2, 4))

print("-" * 50)


# -------------------------------------------------------
# 7. Optimized Calculation Example
# -------------------------------------------------------

print("7️⃣ Optimized Calculation\n")

# Large array
large = np.arange(1_000_000)

start = time.time()
result = np.sum(large)
print("Sum using NumPy:", result)
print("Time taken:", time.time() - start)

print("-" * 50)


# -------------------------------------------------------
# 8. Visualize Array Structure
# -------------------------------------------------------

print("8️⃣ Visualizing Array Structure\n")

print("Array:\n", arr2)
print("Shape:", arr2.shape)
print("Size (Total elements):", arr2.size)
print("Data Type:", arr2.dtype)
print("Memory Used (bytes):", arr2.nbytes)

print("\n===== END OF PROGRAM =====")
