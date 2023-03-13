n, m = map(int, input().split())
node_data = dict()
dop_ans = set()
ans = list()
for i in range(m):
    beg, end = map(int, input().split())
    if end not in node_data:
        node_data[end] = set()
    if beg not in node_data:
        node_data[beg] = set()
    node_data[beg].add(end)
    dop_ans.add(end)
    dop_ans.add(beg)
for j in range(1, n + 1):
    if j not in dop_ans:
        ans.append(j)
while len(node_data) > 0:
    key = None
    flag = False
    for key, value in node_data.items():
        if len(value) == 0:
            flag = True
            ans.append(key)
            for key1, value1 in node_data.items():
                if key in value1:
                    node_data[key1].remove(key)
            break
    if flag:
        del node_data[key]
    else:
        ans = [-1]
        break
if len(ans) == 0:
    ans = [-1]
print(*ans[::-1])
