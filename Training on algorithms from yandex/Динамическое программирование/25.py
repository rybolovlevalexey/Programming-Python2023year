n = int(input())
coords = sorted(map(int, input().split()))
dp = list(None for i in range(n))
dp[0] = 0
dp[1] = coords[1] - coords[0]
for i in range(2, n):
    if i == 2:
        dp[i] = dp[i - 1] + coords[i] - coords[i - 1]
    else:
        dp[i] = min(dp[i - 1], dp[i - 2]) + coords[i] - coords[i - 1]
print(dp[-1])