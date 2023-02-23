def func(pi):
    global n
    end = n
    delta = n // 2
    while True:
        if end == 1:
            if diego[end] < pi:
                return 1
            else:
                if diego[0] < pi:
                    return 0
                return -1
        ind = end - delta
        print("ind", ind)
        while ind >= n:
            ind -= 1
        delta //= 2
        if delta == 0:
            delta = 1
        elem = diego[ind]
        if elem == pi:
            return ind - 1
        if elem > pi and diego[ind - 1] < pi:
            return ind - 1
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
