import numpy as np

# #attributes
# arr_2D=np.array([[1,2,3],
#                  [4,5,6]])
# print(arr_2D.shape)       #shape-gives numbers of rows and column in array

# #size-shows total number of elements in an array
# arr_2D=np.array([[1,2,3],
#                  [4,5,6]])
# print(arr_2D.size) 

#ndim-no.of dimension
# arr_1D=np.array([1,2,3])
# arr_2D=np.array([[1,2,3],[4,5,6]])
# arr_3D=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# print(arr_1D.ndim)
# print(arr_2D.ndim) 
# print(arr_3D.ndim) 

# dtype-return data type of elements
# arr=np.array([10,20,30.3,40])
# print(arr.dtype)

#changing the type of data in other type
#astype(newtype)
# arr=np.array([1.2,2.4,4.1])
# new=arr.astype(int)
# print(new)
# print(new.dtype)


#operators-  +,-,*,/,**,//
# arr=np.array([2,4,6])
# print(arr+5)
# print(arr*5)
# print(arr**2)

#aggregation function-sum,min,max,mean,std,var(variance)
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("sum:",np.sum(arr))
print("min:",np.min(arr))
print("max:",np.max(arr))
print("mean:",np.mean(arr))
print("std:",np.std(arr))
print("var:",np.var(arr))
