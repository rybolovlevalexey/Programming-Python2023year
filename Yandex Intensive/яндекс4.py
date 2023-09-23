k, n, m = map(int, input().split())  # кол-во тротуаров, раскопок, укладок
plitky = dict()
for i in range(n):
    day, num = map(int, input().split())
    if num not in plitky:
        plitky[num] = list()
    plitky[num].append(day)
if n <= m:
    print(0)
elif len(plitky) > m:
    print(-1)
else:
    keys = sorted(plitky.keys(), key=lambda x: len(plitky[x]))
