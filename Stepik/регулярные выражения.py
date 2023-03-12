import json

st = input()
data = json.loads(st)
# (имя, родители, дети)
sp_classes = dict()
for elem in data:
    name = elem["name"]
    parents = elem["parents"]
    sp_classes[name] = set()
    if len(parents) != 0:
        sp_classes[name] = set()
        for paren in parents:
            sp_classes[name].add(paren)

for key in sp_classes.keys():
    stack = list(sp_classes[key])
    while len(stack) > 0:
        par = stack.pop(0)
        sp_classes[key].add(par)
        for new_par in sp_classes[par]:
            if new_par not in stack and new_par not in sp_classes[key]:
                stack.append(new_par)
print(sp_classes)

for name in sorted(sp_classes.keys()):
    cnt = 1
    for sp in sp_classes.values():
        if name in sp:
            cnt += 1
    print(f"{name} : {cnt}")
