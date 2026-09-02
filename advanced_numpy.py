import numpy as np
#insert syntax-np.inset(array,index,value)
#array-original array
#index-postion
#value-actual data to insert
# arr=np.array([10,20,30,40,50,60,70,80,90])
# ind=np.insert(arr,1,15)
# print(ind)

# append
# arr=np.array([10,20,30,40,50,60,70,80,90])
# ind=np.append(arr,[11,12,13,14])
# print(ind)

#concat
# np.concatenate ((array1, array2),axis=0)
#axis 0-vertical stacking
#axis 1-horizontal stacking
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# new_arr=np.concatenate((arr1,arr2))
# print(new_arr)

#removing elements from array
#np.delete([index])
# arr=np.array([10,20,30,40,50,60,70,80,90])
# rem=np.delete(arr,5)
# print(rem)

#removing element in 2D array
# arr_2D=np.array([[1,2,3],[4,5,6]])
# rem=np.delete(arr_2D,5)
# print(rem)

#stacking (vstack,hstack) 
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# print(np.vstack(((arr1,arr2))))
# print(np.hstack(((arr1,arr2))))

#splitting(hsplit(),vsplit())
#syntax-np.split(array,size)
arr=np.array([10,20,30,40,50,60,70,80])
# print(np.split(arr,2))
print(np.split(arr,4))

#discount
# price=np.array([100,200,300,400,500])
# discount=10
# final_price =price-(price*discount/100)
# print(final_price)

#three rules of broad casting
#1.matching dimensions   2.expanding sinle elements    3.incompatible shapes
# arr=np.array([100,200,300])
# result=arr*2
# print(result)

#apply broadcasting to convert 1D array to 2D array
#1.matching dimensions
# matrix=np.array([[1,2,3],[4,5,6]])
# vector=np.array([10,20,30])
# result=matrix+vector
# print(result)

# 2.expanding sinle elements 
# matrix=np.array([[1,2,3],[4,5,6]])
# vector=np.array(10)
# result=matrix+vector
# print(result)

#errors  3.incompatable shape
# matrix=np.array([[1,2,3],[4,5,6]])
# vector=np.array([10,20])
# result=matrix+vector
# print(result)

#vectorization-performing calculation without loops
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# result=arr1+arr2
# print(result)
