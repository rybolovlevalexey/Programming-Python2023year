n, m = map(int, input().split())
result = list([None] * m for i in range(n))
field = list()
for i in range(n):
    line = list(map(int, input().split()))
    field.append(line)
result[0][0] = field[0][0]
for i in range(1, n):
    result[i][0] = result[i - 1][0] + field[i][0]
for j in range(1, m):
    result[0][j] = result[0][j - 1] + field[0][j]
for i in range(1, n):
    for j in range(1, m):
        result[i][j] = min(result[i - 1][j], result[i][j - 1]) + field[i][j]
print(result[-1][-1])