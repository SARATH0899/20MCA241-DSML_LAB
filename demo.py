import numpy as np
matrix_A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
matrix_B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

# sumof matrix
sum_matrix=matrix_A+matrix_B
print("SUM OF MATRIX: ")
print(sum_matrix)
print(" ")

# multiplication of matrix
m_matrix=matrix_A*matrix_B
print("MULTIPLICATION OF MATRIX")
print(m_matrix)
print(" ")

# dot product
dot_matrix=np.dot(matrix_A,matrix_B)
print(" DOT PRODUCT OF MATRIX")
print(dot_matrix)
print(" ")

# transpose ofa matrix of Matrix A
transpose_A=matrix_A.transpose()
print(" Transpose OF MATRIX A")
print(transpose_A)
print(" ")

# Determinant of B
determinant_B=np.linalg.det(matrix_B)
print(" Determinant OF MATRIX B")
print(determinant_B)
print(" ")

# eigenvalues and eigenvectors of matrix_A
eigenvalues_A , eigenvectors_A = np.linalg.eig(matrix_A)
# printing eigen values
print("The Eigen values of Matrix A :\n",eigenvalues_A)
print(" ")
# printing eigen vectors
print("Printing eigenvectors of Matrix A :\n",eigenvectors_A)
print(" ")

# SVD of a matrix
U, D, V = np.linalg.svd(matrix_A)
print("SVD OF A MATRIX")
print(U)
print(D)
print(V)