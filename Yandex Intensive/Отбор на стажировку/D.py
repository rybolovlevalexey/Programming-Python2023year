n = int(input())  # кол-во стран
can_dohod = list(map(int, input().split()))  # минимальный доход
can_obraz = list(map(int, input().split()))  # необходимость образования
can_child = list(map(int, input().split()))  # может ли ребёнок переехать
q = int(input())
dohod = map(int, input().split())
obraz = map(int, input().split())
parents = map(int, input().split())
for j in range(q):
    dj, oj, pj = dohod.__next__(), obraz.__next__(), parents.__next__()
    ans = list()
    if pj != 0 and can_child[pj - 1] != 0:
        ans.append(pj)
    for i in range(n):
        if dj >= can_dohod[i] and oj >= can_obraz[i]:
            ans.append(i + 1)
            break
    if len(ans) == 0:
        print(0, end=" ")
    else:
        print(min(ans), end=" ")
