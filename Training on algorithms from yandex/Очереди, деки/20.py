n = int(input())
sp = list()
ind = 0
for elem in map(int, input().split()):
    sp.append(elem)
    pos = ind
    father = (pos - 1) // 2
    while pos > 0 and sp[father] > sp[pos]:
        sp = sp[:father] + [sp[pos]] + sp[father:]
        sp.pop(pos + 1)
        pos = father
        father = (pos - 1) // 2
    if pos != 0:
        last_ind = (pos - 1) // 2
        while pos >= last_ind and pos - 1 > 0 and sp[pos - 1] > sp[pos]:
            sp[pos - 1], sp[pos] = sp[pos], sp[pos - 1]
            pos -= 1
    ind += 1
print(*sp)