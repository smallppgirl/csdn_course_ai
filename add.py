import numpy as np

def my_add(a, b):
    a = a.copy()
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a[i, j] += b[i, j]
    return a

a = np.array([[1, 1],
              [1, 1]])
b = np.array([[1, 2],
              [3, 4]])

c = my_add(a, b)
d = a + b

a = np.array([[1, 1],
              [2, 2]])
b = np.array([3, 4])
dotab = np.dot(a, b)