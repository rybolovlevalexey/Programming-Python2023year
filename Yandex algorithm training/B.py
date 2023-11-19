from random import randint


def partition(left, right, num):
    
    return 1


def _sort(begin, end):
    global n
    x = sp[randint(0, n - 1)]
    p = partition(begin, end, x)
    _sort(begin, p)
    _sort(p + 1, end)


n = int(input())
sp = list(map(int, input().split()))
_sort(0, n - 1)
print(sp)