n, m, k = map(int, input().split())
matrix = list()
for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)
for i in range(k):
    summa = 0
    x1, y1, x2, y2 = list(i - 1 for i in map(int, input().split()))
    x = x1
    while y1 <= y2:
        while x1 <= x2:
            summa += matrix[x1][y1]
            x1 += 1
        y1 += 1
        x1 = x
    print(summa)