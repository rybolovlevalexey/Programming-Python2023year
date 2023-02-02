n = int(input())
sp = list(map(int, input().split()))
ans = 0
sr = sum(sp) / n
for elem in sp:
    if elem < sr:
        ans += 1
print(ans)