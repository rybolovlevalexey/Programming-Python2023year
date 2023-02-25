n, k = map(int, (input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(1, k+1):
        if i - j < 0:
            break
        dp[i] += dp[i - j]
print(dp[-1])