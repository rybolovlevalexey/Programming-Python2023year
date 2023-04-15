n, x, t = map(int, input().split())  # кол-во скульптур, идеальный лёд, время
sp = map(int, input().split())
ans = 0
ans_sp = list()
razn = dict()  # время на каждую скульптуру
for i in range(1, n + 1):
    razn[i] = abs(x - sp.__next__())
rever_razn = dict()
for key, value in razn.items():
    if value in rever_razn:
        rever_razn[value] += [key]
    else:
        rever_razn[value] = [key]

for elem in sorted(razn.values()):
    if t - elem >= 0:
        ans += 1
        t -= elem
        ans_sp.append(rever_razn[elem].pop())
    else:
        break
print(ans)
print(*sorted(ans_sp))