n = int(input())
tree = dict()  # номер узла: (номер предка, список потомков)
for i in range(n - 1):
    first, second = (map(int, input().split()))
    if first not in tree:
        tree[first] = (None, list())
    tree[first][1].append(second)
    if second not in tree:
        tree[second] = (first, list())
    cur = tree[first][0]
    while cur is not None:
        tree[cur][1].append(second)
        cur = tree[cur][0]
ans = list()
for key in sorted(tree.keys()):
    ans.append(len(tree[key][1]) + 1)
print(*ans)
