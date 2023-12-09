st = input()
flag = True
ans = ""
mid = len(st) // 2
for i in range(mid):
    if flag and st[i] > "a":
        flag = False
        ans = st[:i] + "a" + st[i + 1:]
        break
if len(st) <= 1:
    print()
elif not flag:
    print(ans)
else:
    print(st[:-1] + "b")