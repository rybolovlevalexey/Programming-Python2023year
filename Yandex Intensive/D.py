sp = list(map(int, input().split()))
for i in range(len(sp) // 2 + 1):
    if sp.count(i + 1) == 1:
        print(i + 1)
        break