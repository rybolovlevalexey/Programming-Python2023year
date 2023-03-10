def dfs(graph, now):
    ans.append(now)
    sp_visit[now] = True
    for neigh in graph.get(now, list()):
        if not sp_visit.get(neigh, True):

            dfs(graph, neigh)


file = open("16.txt", "r")
n, m = map(int, file.readline().split())
sp_svz = dict()
for i in range(m):
    first, second = map(int, file.readline().split())
    if first == second and first in sp_svz and second in sp_svz:
        continue
    if first in sp_svz:
        sp_svz[first].add(second)
    else:
        sp_svz[first] = {second}
    if second in sp_svz:
        sp_svz[second].add(first)
    else:
        sp_svz[second] = {first}

ans_ans = list()
sp_visit = dict()
for key in range(1, n + 1):
    sp_visit[key] = False
while False in sp_visit.values():
    ans = list()
    now = min(sp_visit.keys())
    try:
        dfs(sp_svz, now)
    except Exception:
        print(sp_svz, now)
    ans_ans.append(sorted(ans))
    for elem in ans:
        del sp_visit[elem]

print(len(ans_ans))
for elem in ans_ans:
    print(len(elem))
    print(*elem)
