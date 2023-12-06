import numpy as np

## 실습1
vector_ex = np.array([1, 2, 3, 4])
print(vector_ex)

##실습2
matix_a = np.array([[1,2,3], [4, 5, 6]])
print(matix_a)

##실습3
matrix_f = np.array([[1, 2],[3, 4]])
print(matrix_f)

print('\n')

matrix_f_transpose = np.transpose(matrix_f)
print(matrix_f_transpose)

##실습4
matrix_g = np.array([[1, 2], [3, 4]])
print(matrix_g)

print("\n")

matrix_g_1D_flatten = matrix_g.flatten()
print('using flatten:', matrix_g_1D_flatten)

matrix_g_1D_reshape = matrix_g.reshape(1,4)
print('using reshape:', matrix_g_1D_reshape)

##실습5
matrix_i = np.array([1, 2, 3])
matrix_j = np.array([4, 5, 6])
matrix_m = matrix_i * matrix_j
print(matrix_m)

##실습6
matrix_n = np.array([[1, 2],[3, 4]])
matrix_o = np.array([[1, 0],[0, 1]])

matrix_p = np.matmul(matrix_n, matrix_o)
print(matrix_p)

