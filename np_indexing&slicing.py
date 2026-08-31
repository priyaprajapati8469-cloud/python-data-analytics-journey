#indexing -display single value
#slicing-display multiple values
#fancey indexing
#boolean indexing

#access specific element
# arr[index]-1D array
#arr[row,column]-2D array
import numpy as np
# ind=np.array([1,2,3,4,5,6,7,8,9])
# print(ind[5])
# print(ind[-1])



#slicing
# ind=np.array([1,2,3,4,5,6,7,8,9])
# print(ind[2:5:])
# print(ind[::2])
# print(ind[-1::1])

#fency indexing-selecting multiple elements at once (advance)
fen=np.array([1,2,3,4,5,6,7,8,9])
# print(fen[[0,2,2]])

# boolean masking-display the output based on the condition
B=np.array([1,2,3,4,5,6,7,8,9])
print(B[B>6])






