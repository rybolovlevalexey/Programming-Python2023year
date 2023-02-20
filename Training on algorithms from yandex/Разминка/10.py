st = input()
n = len(st)
ans = dict()
for elem in st:
    if elem not in ans:
        ans[elem] = 0
for i in range(n):
    x = i
    y = n - i - 1
    ans[st[i]] += ((x + 1) * (y + 1))
for key in sorted(ans.keys()):
    print(f"{key}: {ans[key]}")