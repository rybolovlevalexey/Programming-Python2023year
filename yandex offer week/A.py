n = int(input())
sp = input().split()
if n % 2 != 0:
    print(-1)
else:
    first, second = sp[: n//2][::-1], sp[n//2:]
    target = None
    while len(first) > 0 and len(second) > 0:
        elem1 = int(first.pop())
        elem2 = int(second.pop())
        if target is None:
            target = elem1 + elem2
        elif elem1 + elem2 != target:
            target = -1
            break
    print(target)
