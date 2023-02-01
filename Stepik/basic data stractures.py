n = int(input())
sp = list(map(int, input().split()))
k = int(input())
for i in range(k, n - 1):
    sp[i] = sp[i + 1]
print(*sp[:-1])