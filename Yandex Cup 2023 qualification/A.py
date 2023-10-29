from pprint import pprint
n, m = map(int, input().split())
benches = list(map(int, input().split()))
sp = list(filter(lambda x: x != 0, benches))
k = len(sp)
matrix = list([0] * k for _ in range(k))
result = 0

if k == 0:
    print(0)
else:
    matrix[0][0] = sp[0]
    for j in range(1, min(k, n + 1)):
        matrix[j][0] = matrix[j - 1][0] + sp[j]
    for i in range(k):
        matrix[i][i] = sp[i]
    for i in range(1, min(k, n)):
        for j in range(i + 1, k):
            matrix[j][i] = matrix[j - 1][i] + sp[j]

    for i in range(k):
        elem = sp[i]
        result += elem**2
        if i + 1 == k:
            continue
        start = i + 1
        end = k - 1 if elem + i + 1 > k else elem + i
        result += matrix[end][start]
    print(result)