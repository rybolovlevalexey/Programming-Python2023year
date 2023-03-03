n = int(input())
dp = list(0 for i in range(n))
a1, a2, a3, b1, b2, b3, c1, c2, c3 = list(0 for i in range(9))
for i in range(n):
    one, two, three = map(int, input().split())
    if i == 0:
        dp[i] = one
        a1, b1, c1 = one, two, three
    elif i == 1:
        a2, b2, c2 = one, two, three
        dp[i] = min(a1 + a2, b2)
    elif i == 2:
        a3, b3, c3 = one, two, three
        dp[i] = min(a1 + a2 + a3, b1 + a3, a1 + b2, c1)
    else:
        dp[i] = min(dp[i - 1] + one, dp[i - 2] + two, dp[i - 3] + three)
print(dp[-1])