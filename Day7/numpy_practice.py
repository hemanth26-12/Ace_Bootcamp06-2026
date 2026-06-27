import numpy as np

a = np.array([[[1,2, 3, 4],[20,21,22,23],[30,31,32,33]],
             [[4,5,6,4],[1,66,77,88],[2,5,6,8]] ,
             [[4,6,5,6],[55,66,88,7],[44,3,2,1]]])


print(a.ndim)
print(a[2][2][0])
print(a.shape)
#print(np.__version__)