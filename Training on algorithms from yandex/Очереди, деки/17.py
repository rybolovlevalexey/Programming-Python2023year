sp1 = list(map(int, input().split()))
sp2 = list(map(int, input().split()))
cnt = 0
while len(sp1) > 0 and len(sp2) > 0 and cnt < 10**6:
    first = sp1.pop(0)
    second = sp2.pop(0)
    if first == 0 and second == 9:
        sp1.append(first)
        sp1.append(second)
    elif first == 9 and second == 0:
        sp2.append(first)
        sp2.append(second)
    else:
        if first > second:
            sp1.append(first)
            sp1.append(second)
        else:
            sp2.append(first)
            sp2.append(second)
    cnt += 1
if len(sp1) == 0:
    print("second", cnt)
else:
    print("first", cnt)