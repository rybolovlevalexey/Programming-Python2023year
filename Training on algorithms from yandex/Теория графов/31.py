def dfs(graph, visited, now):
    global k
    ans.append(now)
    k += 1
    visited[now] = True
    for neigh in graph.get(now, list()):
        if not visited.get(neigh, True):
            dfs(graph, visited, neigh)


n, m = map(int, input().split())
sp_svz = dict()
for i in range(m):
    first, second = map(int, input().split())
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

k = 0
ans = list()
sp_visit = dict()
for key in range(1, n + 1):
    sp_visit[key] = False
now = 1
dfs(sp_svz, sp_visit, now)
print(k)
print(*sorted(ans))