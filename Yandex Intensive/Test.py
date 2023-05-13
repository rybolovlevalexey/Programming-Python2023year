#3.2б
import random

n = int(input("Введите порядок матрицы "))
matrix = list()
for i in range(n):
    line = list()
    for j in range(n):
        line.append(random.randint(-9, 9))
    matrix.append(line)
for line in matrix:
    for i in range(n):
        elem = str(line[i])
        if i == 0:
            print(" " * (2 - len(elem)) + elem, end="")
        else:
            print(" " * (3 - len(elem)) + elem, end="")
    print()
for i in range(n):
    if matrix[i][i] < 0:
        print(f"Наибольший элемент строки {i + 1}: {max(matrix[i])}")
