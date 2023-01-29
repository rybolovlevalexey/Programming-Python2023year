sp = list(map(int, input().split()))
ans = 0
walls = dict()
key = 0
for elem in sp:
    if elem != 0:
        walls[key] = elem
    key += 1
for key1, value in walls.items():
    keys = list(walls.keys())
    keys = keys[keys.index(key1) + 1:]
    for key2 in keys:
        res = (key2 - key1 - 1) * min(value, walls.get(key2))
        if res > ans:
            ans = res
print(ans)