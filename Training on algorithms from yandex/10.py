st = input()
ans = dict()
if st[0] != st[-1]:
    ans[st[-1]] = 1
    ans[st[0]] = 1
else:
    ans[st[0]] = 2
for i in range(0, len(st) - 1):
    for j in range(0, len(st) - 1):
        if len(st) - j <= i:
            break
        res = st[i: len(st) - j]
        for elem in res:
            if elem in ans:
                ans[elem] += 1
            else:
                ans[elem] = 1
for key in sorted(ans.keys()):
    print(f"{key}: {ans[key]}")
