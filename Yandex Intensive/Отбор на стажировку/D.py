n = int(input())  # кол-во стран
can_dohod = map(int, input().split())  # минимальный доход
can_obraz = map(int, input().split())  # необходимость образования
can_child = map(int, input().split())  # может ли ребёнок переехать
country = dict()
for i in range(1, n + 1):
    country[i] = (can_dohod.__next__(), can_obraz.__next__(), can_child.__next__())
mn_doh = min(country.values(), key=lambda x: x[0])[0]
q = int(input())
dohod = map(int, input().split())
obraz = map(int, input().split())
parents = map(int, input().split())
output = list()
for i in range(q):
    ans = set()
    dj, oj, pj = dohod.__next__(), obraz.__next__(), parents.__next__()
    for j in country:
        if dj == 0 and oj == 0 and pj == 0:
            if country[j][0] == 0 and country[j][1] == 0 and (country[j][2] == 0 or country[j][2] == 1):
                ans.add(j)
                break
        if ((dj >= country[j][0]) and (oj - country[j][1] >= 0)) or\
                ((pj == j) and (country[j][2] == 1)):
            ans.add(j)
            break
    if len(ans) == 0:
        output.append(0)
    else:
        output.append(min(ans))
print(*output)