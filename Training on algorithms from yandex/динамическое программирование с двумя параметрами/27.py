n, m = map(int, input().split())
result = list([None] * m for i in range(n))
field = list()
for i in range(n):
    line = list(map(int, input().split()))
    field.append(line)
result[0][0] = (field[0][0], None)
for i in range(1, n):
    result[i][0] = [result[i - 1][0][0] + field[i][0], "D"]
for j in range(1, m):
    result[0][j] = [result[0][j - 1][0] + field[0][j], "R"]
for i in range(1, n):
    for j in range(1, m):
        result[i][j] = [max(result[i - 1][j][0], result[i][j - 1][0]) + field[i][j], None]
        if result[i - 1][j][0] > result[i][j - 1][0]:
            result[i][j][1] = "D"
        else:
            result[i][j][1] = "R"
print(result[-1][-1][0])
i = n - 1
j = m - 1
ans = ""
while i > 0 or j > 0:
    ans += result[i][j][1] + " "
    if result[i][j][1] == "D":
        i -= 1
    else:
        j -= 1
print(ans.strip()[::-1])
