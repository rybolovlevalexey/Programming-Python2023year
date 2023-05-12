#3.2
import random

# вариант с ручным вводом матрицы
n = int(input("Введите кол-во строк матрицы "))
m = int(input("Введите кол-во столбцов матрицы "))
matrix = list()
#print("Введите матрицу")
#for i in range(n):
#    line = list()
#    for elem in input().split():
#        line.append(int(elem))
#    matrix.append(line)
# вариант с рандомным заданием исходной матрицы
print("Матрица A:")
for i in range(n):
    line = list()
    for j in range(m):
        elem = random.randint(-9, 9)
        line.append(elem)
        elem = str(elem)
        if j != 0:
            print(" " * (4 - len(elem)) + elem, end="")
        else:
            print(" " * (2 - len(elem)) + elem, end="")
    matrix.append(line)
    print()

print("Матрица B:")
answer = list()
for i in range(n):
    answer.append(sorted(matrix[i])[::-1])
for line in answer:
    for j in range(m):
        elem = str(line[j])
        if j != 0:
            print(" " * (4 - len(elem)) + elem, end="")
        else:
            print(" " * (2 - len(elem)) + elem, end="")
    print()