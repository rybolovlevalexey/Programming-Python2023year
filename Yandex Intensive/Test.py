import random

n = int(input("Введите кол-во строк в массиве "))
m = int(input("Введите кол-во столбцов в массиве "))
matrix = list(list(random.randint(-10, 10) for j in range(m)) for i in range(n))
print(*matrix, sep="\n")

num = int(input("Введите интересующий номер столбца "))
if num < 1 or num > m:
    print("Введён неверный номер столбца")
else:
    summ = 0
    for i in range(n):
        summ += matrix[i][num - 1]
    print(f"Среднее арифметическое {num}-того столбца: {summ / n}")