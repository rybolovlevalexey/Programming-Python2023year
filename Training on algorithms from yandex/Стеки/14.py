stack = list()
n = int(input())
cnt = 0
#flag = True
for elem in map(int, input().split()):
    if elem - 1 != cnt:
        stack.append(elem)
    else:
        cnt += 1
    while len(stack) > 0 and stack[-1] - 1 == cnt:
        cnt += 1
        del stack[-1]
if len(stack) == 0:
    print("YES")
else:
    print("NO")