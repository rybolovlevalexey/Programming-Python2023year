m = int(input())
n = int(input())
sp = list()
sp1 = list()
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    j = 0
    while j < cnt:
        aj, bj = sp[j]
        if bj >= a >= aj or (aj <= b and bj >= a):
            del sp[j]
            cnt -= 1
        else:
            j += 1
    sp.append((a, b))
    cnt += 1
print(cnt)
