# (имя, родители, дети)
sp_classes = dict()
n = int(input())
for i in range(n):
    stroka = input().strip()
    if ":" not in stroka:
        sp_classes[stroka] = set()
    else:
        name, parents = stroka.split(" : ")
        sp_classes[name] = set(parents.split())
for key in sp_classes.keys():
    stack = list(sp_classes[key])
    while len(stack) > 0:
        par = stack.pop(0)
        sp_classes[key].add(par)
        for new_par in sp_classes[par]:
            if new_par not in stack and new_par not in sp_classes[key]:
                stack.append(new_par)
#print(sp_classes)

m = int(input())
for i in range(m):
    first, second = input().split()
    if first in sp_classes and second in sp_classes and \
            (first in sp_classes[second] or first == second):
        print("Yes")
    else:
        print("No")
