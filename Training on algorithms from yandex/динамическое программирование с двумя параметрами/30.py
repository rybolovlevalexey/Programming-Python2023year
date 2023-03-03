n = int(input())
st1 = input().split()
m = int(input())
st2 = input().split()
result = list([0] * n for i in range(m))
flag = False
for i in range(n):
    if flag or st1[i] == st2[0]:
        flag = True
        result[0][i] = 1
    else:
        result[0][i] = 0
flag = False
for j in range(m):
    if flag or st2[j] == st1[0]:
        flag = True
        result[j][0] = 1
    else:
        result[j][0] = 0
for i in range(1, n):
    flag = False
    for j in range(1, m):
        if max(result[i - 1][j], result[i][j - 1]) == i + 1 or \
                max(result[i - 1][j], result[i][j - 1]) == j + 1:
            result[i][j] = max(result[i - 1][j], result[i][j - 1])
        else:
            if flag:
                result[i][j] = i + 1
            else:
                if st1[j] == st2[i]:
                    result[i][j] = max(result[i - 1][j], result[i][j - 1]) + 1
                    if result[i][j] == i + 1:
                        flag = True
                else:
                    result[i][j] = max(result[i - 1][j], result[i][j - 1])

print(*result, sep="\n")