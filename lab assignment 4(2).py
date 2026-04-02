import numpy as np

matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

addition = matrix1 + matrix2
multiplication = np.matmul(matrix1, matrix2)

print("\nAddition of Matrices:")
print(addition)

print("\nMatrix Multiplication:")
print(multiplication)
