import numpy as np
import pandas

list_2d = [[1,2,1],[3,0,1],[0,2,4]]
list_1 = [[3,5,4],[7,8,3],[2,8,9]]
print(list_2d)

mat_2d = np.array(list_2d)
mat1 = np.array(list_1)
print("2d numpy array: \n", mat_2d)
print("ndim: ", mat_2d.ndim) #2 -> rows x columns
print("shape: ", mat_2d.shape) # 3 x 3 -> (3, 3)
print("size: ", mat_2d.size) #9
mat_sum = mat_2d + mat1
print(mat_sum)
mat_sub = mat_2d - mat1
print(mat_sub)
mat_mul1 = np.dot(mat_2d, mat1)
mat_mull2 = mat_2d.dot(mat1)
mat_mull3 = np.matmul(mat_2d,mat1)
print(mat_mul1, '\n')
print(mat_mull2, '\n')
print(mat_mull3, '\n')
element_wise_mult = mat_2d * mat1
print(element_wise_mult)
doubled_mat = 2 * element_wise_mult
print(doubled_mat)
vec = np.array([1,2,3,4,5])
print(vec.ndim)
print(vec[3])