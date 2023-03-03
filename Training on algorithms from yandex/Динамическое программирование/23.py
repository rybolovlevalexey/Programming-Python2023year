# индекс - соответствующее число
n = int(input())
dp = list([0, 0, 0] for i in range(n + 1))
dp[1] = [1, 0, 0]  # (кол-во способов, номер операции, из какого числа пришёл)
for i in range(2, n + 1):
    dp[i][0] += dp[i - 1][0]
    if i % 2 != 0 and i % 3 != 0:
        dp[i][1] = dp[i - 1][1] + 1
        dp[i][2] = i - 1
    if i % 2 == 0 and i % 3 != 0:
        dp[i][0] += dp[i // 2][0]
        dp[i][1] = min(dp[i - 1][1], dp[i // 2][1]) + 1
        if dp[i - 1][1] < dp[i // 2][1]:
            dp[i][2] = i - 1
        else:
            dp[i][2] = i // 2
    if i % 3 == 0 and i % 2 != 0:
        dp[i][0] += dp[i // 3][0]
        dp[i][1] = min(dp[i - 1][1], dp[i // 3][1]) + 1
        if dp[i - 1][1] < dp[i // 3][1]:
            dp[i][2] = i - 1
        else:
            dp[i][2] = i // 3
    if i % 3 == 0 and i % 2 == 0:
        dp[i][0] += (dp[i // 2][0] + dp[i // 3][0])
        dp[i][1] = min(dp[i - 1][1], dp[i // 3][1], dp[i // 2][1]) + 1
        if dp[i - 1][1] < dp[i // 2][1] and dp[i - 1][1] < dp[i // 3][1]:
            dp[i][2] = i - 1
        elif dp[i // 2][1] < dp[i // 3][1]:
            dp[i][2] = i // 2
        else:
            dp[i][2] = i // 3

print(dp[-1][1])
ans = ""
k = n
while k > 0:
    ans += str(k) + " "
    k = dp[k][2]
print(ans.strip()[::-1])