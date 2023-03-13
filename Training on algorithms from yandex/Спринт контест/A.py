n = int(input())
train = list()
# (наименование товара, кол-во вагонов)
for i in range(n):
    st = input().split()
    if st[0] == "add":
        cnt, name = st[1], st[2]
        train.append([name, int(cnt)])
    elif st[0] == "delete":
        cnt = int(st[1])
        while cnt > 0:
            if train[-1][1] > cnt:
                train[-1][1] -= cnt
                cnt = 0
            elif train[-1][1] == cnt:
                cnt = 0
                del train[-1]
            else:
                cnt -= train[-1][1]
                del train[-1]
    else:
        name = st[1]
        cnt = 0
        for elem in train:
            if elem[0] == name:
                cnt += elem[1]
        print(cnt)
