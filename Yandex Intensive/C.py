sp = map(int, input().split())
mn1 = set()
mn2 = set()
for elem in sp:
    if elem in mn1:
        mn2.add(elem)
    else:
        mn1.add(elem)
if len(mn1) not in mn2:
    print(len(mn1))
else:
    nums = sorted(mn2)
    for i in range(len(mn2) - 1):
        if nums[i + 1] - nums[i] != 1:
            print(i + 2)
            break