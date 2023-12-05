import numpy as np

array = np.loadtxt("file_name.txt")
k = int(input()) - 1
col_num = list(np.where(array[k] == array[k].min()))[0]
summa = sum(filter(lambda x: x < 0, array[:, col_num]))
print(*summa)