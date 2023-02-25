n = int(input())
change = False
flag = True
prev = None
ind = 0
for elem in map(int, input().split()):
    if prev is None:
        prev = elem
    else:
        if not change and prev > elem and ind != 1:
            change = True
            prev = elem
        elif not change and prev < elem:
            prev = elem
        elif change and prev > elem:
            prev = elem
        else:
            flag = False
            break
    ind += 1
if flag and change:
    print("YES")
else:
    print("NO")