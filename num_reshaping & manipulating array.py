#reshape(rows,columns) specify shape,if dimension match
import numpy as np
## convert 1D array into 2D or multi dimentional array
# arr=np.array([1,2,3,4,5,6,7,8])
# reshaped_arr=arr.reshape(2,4)    #2-row   4-column
# print(reshaped_arr)    # does not creat copy reshape effect original values

#flattening array-convert 2D array into 1D array
#1.ravel()-provide view of original data
#2.flatten()-provide copy of original data
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])   
print(arr_2d.ravel())
print(arr_2d.flatten())