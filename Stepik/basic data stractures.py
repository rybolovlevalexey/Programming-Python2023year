n = int(input())
sp = list(map(int, input().split()))
k, x = map(int, input().split())
for i in range(k, n):
    sp[i], x = x, sp[i]
sp.append(x)
print(*sp)
