import bisect

def func(pi):
    global n
    end = n // 2
    delta = n // 4
    while True:
        if end == 1:
            if diego[end] < pi:
                return 1
            else:
                if diego[0] < pi:
                    return 0
                return -1
        elem = diego[end - delta]
        if elem == pi or diego[end - delta - 1] < pi < elem:
            ind = end - delta
            return ind - 1

        delta //= 2
        if delta == 0:
            delta = 1
        if elem < pi:
            end = end + delta
        else:
            end = end - delta


int(input())
diego = tuple(set(map(int, input().split())))
mx = max(diego)
mn = min(diego)
n = len(diego)
k = int(input())

for collector in map(int, input().split()):
    if n == 1:
        print(1 if diego[0] < collector else 0)
    elif mx < collector:
        print(n)
    elif mx == collector:
        print(n - 1)
    elif mn >= collector:
        print(0)
    else:
        print(func(collector) + 1)
