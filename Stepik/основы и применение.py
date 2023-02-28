# (имя, родители, дети)
sp_classes = dict()
n = int(input())
for i in range(n):
    stroka = input().strip()
    if ":" not in stroka:
        sp_classes[stroka] = []
    else:
        name, parents = stroka.split(" : ")
        sp_classes[name] = parents.split()
        for par in parents:
            sp_classes[name].extend(sp_classes.get(par, []))

print(sp_classes)
m = int(input())
for i in range(m):
    first, second = input().split()
    if first in sp_classes and second in sp_classes and \
            (first in sp_classes[second] or first == second):
        print("Yes")
    else:
        print("No")
