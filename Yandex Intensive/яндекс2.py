n, k = map(int, input().split())  # всего, можно не использовать
sp = sorted(map(int, input().split()))
ans = sp[n - k - 1] - sp[0]
first = 0
last = n - k - 1
while first <= k:
    ans = min(ans, sp[last] - sp[first])
    first += 1
    last += 1
print(ans)