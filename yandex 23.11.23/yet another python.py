n = int(input())
sp = list(int(elem.split(":")[0]) * 60 + int(elem.split(":")[1]) for elem in input().split())
sp.extend(list(map(lambda x: x + 1440, sp)))
sp = sorted(sp)
ans = None
for i in range(0, len(sp) - 1):
    if ans is None or sp[i + 1] - sp[i] < ans:
        ans = sp[i + 1] - sp[i]
print(ans)
