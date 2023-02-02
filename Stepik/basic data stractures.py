n = int(input())
sp = list(map(int, input().split()))
ans = 0
for i in range(1, n, 2):
    if sp[i] > 0:
        ans += sp[i]
print(ans)