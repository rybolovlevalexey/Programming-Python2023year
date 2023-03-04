n = int(input())
dp = list(0 for i in range(n))
dp[0] = 2

for i in range(1, n):
    if i == 1:
        dp[i] = 4
    elif i == 2:
        dp[i] = 7
    else:
        dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]
print(dp[-1])
