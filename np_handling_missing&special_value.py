#np.isnan-detect missing values  syntax-np.isnan(array)
#np.nan_to_num()-replace values   synatx-nan_to_num(array,nan=value)
#np.isinf-detect infinite values

import numpy as np
#1.  np.isnan()
# arr=np.array([10,20,np.nan,40])
# print(np.isnan(arr))

#2. np.nan_to_num()
# arr=np.array([10,20,np.nan,40])
# print(np.nan_to_num(arr,nan=5))

#3.np.isinf()
arr=np.array([10,20,-np.inf,40])
print(np.isinf(arr))
cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_arr)