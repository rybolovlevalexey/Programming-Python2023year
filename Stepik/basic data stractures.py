n, m = map(int, input().split())
num = 1
i = j = 0
start_j = start_i = 0
sp = list([None] * m for _ in range(n))
while num <= n * m:
    sp[i][j] = num
    num += 1
    i += 1
    j -= 1
    if i >= n or j < 0:
        if start_j + 1 < m:
            start_j += 1
            j = start_j
            i = 0
        else:
            start_i += 1
            i = start_i
            j = m - 1
for i in range(n):
    for j in range(m):
        elem = str(sp[i][j])
        print((3 - len(elem)) * " " + elem, end="")
    print()
