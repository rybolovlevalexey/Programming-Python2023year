def func(pi):
    global n
    end = n
    while True:
        if end == 1:
            if diego[end] < pi:
                return 1
            else:
                if diego[0] < pi:
                    return 0
                return -1
        ind = end // 2
        elem = diego[ind]
        if elem == pi:
            #print("here 11")
            return ind - 1
        if elem > pi and diego[ind - 1] < pi:
            #print("here12")
            return ind - 1
        if elem < pi:
            end = (end + ind) // 2
        else:
            end = ind


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
        #print("here1", end=' ')
        print(n)
    elif mx == collector:
        print(n - 1)
    elif mn >= collector:
        #print("here2", end=' ')
        print(0)
    else:
        #print("here3", end=' ')
        print(func(collector) + 1)
