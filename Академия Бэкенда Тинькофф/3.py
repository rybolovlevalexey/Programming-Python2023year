n, m, q = map(int, input().split())
field = list()
for i in range(n):
    line = tuple(map(int, input().split()))
    field.append(line)

for j in range(q):
    x, y, k = map(int, input().split())
    x -= 1
    y -= 1
    cur = field[x][y]
    ans = 0
    for t in range(min(n, m)):
        if t != y and abs(field[x][t] - cur) <= k:
            ans += 1
        if t != x and abs(field[t][y] - cur) <= k:
            ans += 1
    if m > n:
        for t in range(n, m):
            if t != y and abs(field[x][t] - cur) <= k:
                ans += 1
    if n > m:
        for t in range(m, n):
            if t != x and abs(field[t][y] - cur) <= k:
                ans += 1
    print(ans)