import numpy as np


mat = np.matrix([[0 for i in range(49)]]).reshape(7, 7)
print(mat)

for i in range(7):
    mat[i, i] = (i+1)**2
print(mat)

for i in range(4):
    mat[i, i+3] = i+1
print(mat)

for i in range(6):
    mat[i+1, i] = (i+2)+(i+1)
print(mat)

mat[4] = mat[4]+2
print(mat)

tmat = mat.T
print(tmat)

print(mat@tmat) #або print(mat.dot(tmat))
