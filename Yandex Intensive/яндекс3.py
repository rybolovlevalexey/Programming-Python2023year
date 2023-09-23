class Answer:
    number: int = None  # номер репозитория
    count: int = None  # кол-во репозиториев до данного


repos = dict()  # номер репа: [номер родителя, кол-во до данного]
n = int(input())
ans = Answer
for i in range(1, n + 1):
    parent = int(input())
    cnt = -1
    if parent == 0:
        repos[i] = [parent, 1]
        cnt = 1
    else:
        cnt = repos.get(parent)[1] + 1
        repos[i] = [parent, cnt]

    if ans.count is None or cnt > ans.count:
        ans.count = cnt
        ans.number = i

print(ans.number)
