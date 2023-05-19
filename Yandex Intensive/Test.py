#3.2
import random

n = int(input("Введите кол-во строк матрицы "))
m = int(input("Введите кол-во столбцов матрицы "))
matrix = list()
# вариант с рандомным заданием исходной матрицы
print("Матрица A:")
for i in range(n):
    line = list()
    for j in range(m):
        elem = random.randint(10, 99)
        line.append(elem)
        print(elem, end=" ")
    matrix.append(line)
    print()

print("Матрица B:")
answer = list()
for i in range(n):
    answer.append(sorted(matrix[i])[::-1])
for line in answer:
    for j in range(m):
        elem = str(line[j])
        print(elem, end=" ")
    print()
