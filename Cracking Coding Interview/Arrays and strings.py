import numpy as np

a = np.arange(1, 8)
b = a[:]
b[2] = 10
print(a)
print(b)
