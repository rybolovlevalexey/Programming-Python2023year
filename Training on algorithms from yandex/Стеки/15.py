n = int(input())
stack = list()
ans = dict()
ind = 0
# stack -> (значение, индекс)
for elem in map(int, input().split()):
    while len(stack) > 0 and elem < stack[-1][0]:
        ans[stack[-1][1]] = ind
        del stack[-1]
    stack.append([elem, ind])
    ind += 1
for value, ind in stack:
    ans[ind] = -1
for key in sorted(ans.keys()):
    print(ans[key], end=" ")
