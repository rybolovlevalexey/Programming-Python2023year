st = input()
sp = list()
name = None
for i in range(len(st)):
    elem = st[i]
    if elem == "/":
        if name is not None:
            if name == "..":
                if len(sp) > 0:
                    del sp[-1]
            elif name != ".":
                sp.append(name)
            name = None
    else:
        if name is None:
            name = elem
        else:
            name += elem
if name is not None:
    if name == "..":
        if len(sp) > 0:
            del sp[-1]
    elif name != ".":
        sp.append(name)

print("/" + "/".join(sp))
