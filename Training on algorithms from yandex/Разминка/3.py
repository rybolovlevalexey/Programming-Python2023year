import bisect


n = int(input())
diego = sorted(set(map(int, input().split())))
m = int(input())
for collector in map(int, input().split()):
    res = bisect.bisect_left(diego, collector)
    print(res)