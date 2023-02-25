n, m, k = map(int, input().split())
summ_sp = list([None] * m for _ in range(n))
for i in range(n):
    line = list(map(int, input().split()))
    if i == 0:
        summ_sp[0][0] = line[0]
        for j in range(1, m):
            summ_sp[i][j] = line[j] + summ_sp[i][j - 1]
    else:
        for j in range(m):
            if j > 0:
                summ_sp[i][j] = (summ_sp[i-1][j] + summ_sp[i][j - 1] - summ_sp[i-1][j-1] + line[j])
            else:
                summ_sp[i][j] = (int(summ_sp[i - 1][j]) + line[j])
#print(*summ_sp, sep='\n')
for _ in range(k):
    x1, y1, x2, y2 = map(lambda x: x - 1, map(int, input().split()))
    ans = summ_sp[x2][y2]
    if x1 - 1 >= 0:
        ans -= summ_sp[x1 - 1][y2]
    if y1 - 1 >= 0:
        ans -= summ_sp[x2][y1 - 1]
    if x1 - 1 >= 0 and y1 - 1 >= 0:
        ans += summ_sp[x1 - 1][y1 - 1]
    print(ans)