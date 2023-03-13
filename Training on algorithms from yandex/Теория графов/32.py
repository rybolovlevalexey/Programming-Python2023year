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
    # установку в минимальную точку новой компоненты связности
    queue = list()
    sp_visit[now] = True
    queue.extend(sp_svz.get(now, list()))
    while len(queue) > 0:
        node = queue.pop()
        while node in queue:
            queue.remove(node)
        sp_visit[node] = True
        for new_node in sp_svz.get(node, list()):
            if new_node not in queue and not sp_visit.get(new_node, True):
                queue.append(new_node)
    ans_ans.append(sorted(ans))
    for elem in ans:
        del sp_visit[elem]

print(len(ans_ans))
#for elem in ans_ans:
#    print(len(elem))
#    print(*elem)
