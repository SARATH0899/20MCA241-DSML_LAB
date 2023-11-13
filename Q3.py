import numpy as np

matrix_A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

matrix_B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

matrix_sum = matrix_A + matrix_B
matrix_product = matrix_A * matrix_B
matrix_dot = np.dot(matrix_A,matrix_B)
matrix_A_transpose = np.transpose(matrix_A)
determinant_B = np.linalg.det(matrix_B)
eigenvalues_A, eigenvectors_A = np.linalg.eig(matrix_A)

print("Sum of element wise matrix: \n",matrix_sum)
print("Product of element wise matrix: \n",matrix_product)
print("Dot product of matrix: \n",matrix_dot)
print("Transpose of a matrix A: \n",matrix_A_transpose)
print("Determinant of matrix B: ",determinant_B)
print("Eigen value of matrix A: ",eigenvalues_A)
print("Eigen vector of matrix A: \n",eigenvectors_A)
