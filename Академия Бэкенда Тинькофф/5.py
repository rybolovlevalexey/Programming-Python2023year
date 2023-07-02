import itertools

answer = list()  # уродство, сила
n = int(input())
sp = list()
for i in range(n):
    elem = input()
    sp.append(elem)
    ugly = max(elem.count("a"), elem.count("b"), elem.count("c")) - \
           min(elem.count("a"), elem.count("b"), elem.count("c"))
    if len(answer) == 0 or ugly < answer[0]:
        answer = [ugly, len(elem)]
    if answer[0] == ugly and len(elem) > answer[1]:
        answer[1] = len(elem)
for t in range(2, n + 1):
    indexes = itertools.combinations(list(int(i) for i in range(0, n)), t)
    horses = ""
    for coup_indexes in indexes:
        for ind in coup_indexes:
            horses += sp[ind]
        ugly = max(horses.count("a"), horses.count("b"), horses.count("c")) - \
               min(horses.count("a"), horses.count("b"), horses.count("c"))
        if ugly < answer[0]:
            answer[0] = ugly
            answer[1] = len(horses)
        if ugly == answer[0] and answer[1] < len(horses):
            answer[1] = len(horses)
print(answer[1])
