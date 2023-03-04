n = int(input())
st1 = input().split()  # j
m = int(input())
st2 = input().split()  # i
dp = list([0] * n for i in range(m))
ans = ""
for i in range(m):
    elem = st2[i]
    for j in range(n):
        if i == 0 and j == 0:
            if st1[j] == st2[i]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
        else:
            if elem == st1[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
i = m - 1
j = n - 1
#print(*dp, sep="\n")
while i >= 0 and j >= 0:
    if i == 0 and j == 0 and dp[i][j] == 1:
        ans += st1[j]

    if j == 0 and i > 0 and dp[i - 1][j] < dp[i][j]:
        ans += st1[j][::-1] + " "
        j -= 1
    elif (dp[i - 1][j] < dp[i][j] and dp[i][j - 1] < dp[i][j]) or \
            (i == 0 and dp[i][j - 1] < dp[i][j]):
        ans += st1[j][::-1] + " "
        i -= 1
        j -= 1
    elif dp[i][j - 1] < dp[i][j] and dp[i - 1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1
        if j < 0:
            j = n - 1
            i -= 1
print(ans[::-1].strip())
