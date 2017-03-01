# Matrix Algebra

from numpy import matrix, linalg
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1, -1],[0, 1]])
C = np.array([[5, -1], [9, 1], [6,0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1], [8], [0], [5]])

print A.shape, B.shape, C.shape, D.shape, u.shape, v.shape, w.shape
print u+v, u-v, 6*u, u*v, linalg.norm(u)

try:
    print A+C
except ValueError:
    print "Not defined"

try:
    print A-(C.T)
except ValueError:
    print "Not defined"

try:
    print (C.T)+3*D
except ValueError:
    print "Not defined"

try:
    print B.dot(A)
except ValueError:
    print "Not defined"

try:
    print B.dot(A.T)
except ValueError:
    print "Not defined"

try:
    print B.dot(C)
except ValueError:
    print "Not defined"

try:
    print C.dot(B)
except ValueError:
    print "Not defined"

try:
    print linalg.matrix_power(B, 4)
except ValueError:
    print "Not defined"

try:
    print A.dot(A.T)
except ValueError:
    print "Not defined"

try:
    print (D.T).dot(D)
except ValueError:
    print "Not defined"