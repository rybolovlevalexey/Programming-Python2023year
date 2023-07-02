spisok = [5, 3, 2, 6, 4, 1]


def sort1(sp: list) -> list:
    if len(sp) == 1:
        return sp
    if len(sp) == 2:
        if sp[0] < sp[1]:
            return sp
        return [sp[1], sp[0]]
    res = list()
    first = iter(sort1(sp[:len(sp) // 2 + 1]))
    second = iter(sort1(sp[len(sp) // 2 + 1:]))
    a, b = first.__next__(), second.__next__()
    while a is not None or b is not None:
        if a is None:
            res.append(b)
            b = second.__next__()
        elif b is None or a < b:
            res.append(a)
            a = first.__next__()
        else:
            res.append(b)
            b = second.__next__()
    return res

print(sort1(spisok))