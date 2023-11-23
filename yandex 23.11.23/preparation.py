sp = map(int, input().split(", "))
ans_sp = list()
last_elem: [int, None] = None
cur_st: [str, None] = None
elem: int = -1
for elem in sp:
    if last_elem is None:
        last_elem = elem
        cur_st = str(elem)
    else:
        if last_elem + 1 == elem:
            last_elem = elem
        else:
            if str(last_elem) != cur_st:
                cur_st += "-"
                cur_st += str(last_elem)
            ans_sp.append(cur_st)
            cur_st = str(elem)
            last_elem = elem
if cur_st == str(elem):
    ans_sp.append(cur_st)
else:
    cur_st += "-" + str(elem)
    ans_sp.append(cur_st)
print(ans_sp)