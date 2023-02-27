# (название, содержимые элементы, родительские пространства, дочерние)
def func(st):
    if st[0] == "create":
        namespace, parent = st[1], st[2]
        for j in range(len(spaces)):
            if spaces[j][0] == parent:
                spaces[j][3].append(namespace)
                spaces.append((namespace, [], [parent] + spaces[j][2], []))
                return
    elif st[0] == "add":
        namespace, var = st[1], st[2]
        for j in range(len(spaces)):
            if spaces[j][0] == namespace:
                spaces[j][1].append(var)
                return
    else:
        namespace, var = st[1], st[2]
        for j in range(len(spaces)):
            if spaces[j][0] == namespace:
                if var in spaces[j][1]:
                    return namespace
                else:
                    for fath_name in spaces[j][2]:
                        for k in range(len(spaces)):
                            if spaces[k][0] == fath_name:
                                if var in spaces[k][1]:
                                    return fath_name
        return None


spaces = list()
spaces.append(("global", [], [], []))
n = int(input())
for i in range(n):
    stroka = input().strip().split()
    if stroka[0] == "create" or stroka[0] == "add":
        func(stroka)
    else:
        print(func(stroka))
