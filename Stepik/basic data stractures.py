def checking(spisok):
    if len(spisok) == 0:
        return False
    for elem in spisok.split("/"):
        if int(elem.split(",")[1]) >= 3:
            return True
    return False


def make_st(spisok):
    st = ""
    cnt = 1
    for i in range(1, len(spisok)):
        if spisok[i - 1] == spisok[i]:
            cnt += 1
        else:
            st += (str(spisok[i - 1]) + "," + str(cnt) + "/")
            cnt = 1

        if i + 1 == len(spisok):
            st += (str(spisok[i]) + "," + str(cnt) + "/")
    return st[:-1]


def make_small_sp(spisok):
    res = ""
    for elem in spisok:
        a, b = elem.split(",")
        res += a * int(b)
    return res


n = int(input())
sp = list(map(int, input().split()))
ans = 0
st = make_st(sp)
while checking(st):
    i = 0
    st1 = st.split("/")
    while i < len(st1):
        if int(st1[i].split(",")[1]) >= 3:
            ans += int(st1[i].split(",")[1])
            del st1[i]
        else:
            i += 1
    sp1 = make_small_sp(st1)
    st = make_st(sp1)
print(ans)