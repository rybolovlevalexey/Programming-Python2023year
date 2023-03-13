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

ans = list()
sp_visit = dict()
for key in range(1, n + 1):
    sp_visit[key] = False
# старт в первом узле
queue = list()
sp_visit[1] = True
queue.extend(sp_svz.get(1, list()))
# обход всех остальных
while len(queue) > 0:
    node = queue.pop()
    while node in queue:
        queue.remove(node)
    sp_visit[node] = True
    for new_node in sp_svz.get(node, list()):
        if new_node not in queue and not sp_visit.get(new_node, True):
            queue.append(new_node)
for key, value in sp_visit.items():
    if value:
        ans.append(key)
print(len(ans))
print(*ans)