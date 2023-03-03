n, m = map(int, input().split())
field = list([0] * m for i in range(n))
field[0][0] = 1
for i in range(n):
    for j in range(m):
        if i - 1 >= 0 and j - 2 >= 0:
            field[i][j] += field[i - 1][j - 2]
        if i - 2 >= 0 and j - 1 >= 0:
            field[i][j] += field[i - 2][j - 1]
print(field[-1][-1])
