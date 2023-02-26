ans = dict()
for i in range(int(input())):
    st = input()
    if st in ans:
        ans[st] += 1
    else:
        ans[st] = 1
print(sum(filter(lambda x: x != 1, ans.values())))