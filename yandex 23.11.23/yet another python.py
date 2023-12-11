n = int(input())
sp: list[tuple[int]] = list()
for i in range(n):
    time = tuple(map(int, input().split()))
    if len(sp) == 0 or time[1] < sp[0][1] or (time[1] == sp[0][1] and time[0] <= sp[0][0]):
        sp = [time] + sp
        continue
    for j in range(1, i - 1):
        if sp[j - 1][1] < time[1] < sp[j + 1][1] or \
                (sp[j - 1][1] <= time[1] < sp[j + 1][1] and sp[j - 1][0] <= time[0]) or \
                (sp[j - 1][1] < time[1] <= sp[j + 1][1] and time[0] <= sp[j + 1][0]):
            sp.insert(j, time)
            break
    else:
        sp.append(time)
cur_time = None
ans = 0
for elem in sp:
    if cur_time is None or elem[0] >= cur_time[1]:
        cur_time = elem
        ans += 1
print(ans)