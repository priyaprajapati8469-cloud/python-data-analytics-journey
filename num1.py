import numpy as np
# 1D array
# np_array=np.array([1,2,3,4,5])
# print(np_array)

# # 2D array
# np_array=np.array([[1,2,3],
#                    [4,5,6]])
# print(np_array)

# #multidimensional array
# #matrix
# matrix=np.array([[2,4,6],
#                  [8,10,12]])
# print(matrix)

# #creating arrays from python lists
# #synatx-zeros(shape)   shape-size
# zero=np.zeros(3)
# print("zeros")
# print(zero)

# one=np.ones(2)
# print(one)

# #full(shape,values)

# # filled_array=np.full((2,2),"use to fill future values")
# filled_array=np.full(2,"used to fill future values")
# print(filled_array)


# #creating sequence of numbers
# #syntax-arange(start,stop,step)
# arr=np.arange(1,10,2)
# print(arr)

#creating identity matrices
#syntax-eye(size)
identity_mat=np.eye(5)
print(identity_mat)
