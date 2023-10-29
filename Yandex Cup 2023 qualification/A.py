n, m = map(int, input().split())
benches = list(map(int, input().split()))
result = 0
for i in range(m):
    elem = benches[i]
    result += elem**2
    j = i + 1
    while elem > 0:
        if j >= m:
            break
        if benches[j] != 0:
            elem -= 1
        result += benches[j]
        j += 1
print(result)
