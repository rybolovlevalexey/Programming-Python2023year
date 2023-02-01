def checking(spisok):
    for i in range(len(spisok) - 2):
        if spisok[i] == spisok[i + 1] == spisok[i + 2]:
            return True
    return False


ans = 0
n = int(input())
sp = list(map(int, input().split()))
while checking(sp):
    print(sp)
    i = 0
    mem = None
    while i + 2 < len(sp):
        if mem is None and sp[i] == sp[i + 1] == sp[i + 2]:
            mem = sp[i]
            del sp[i]
            ans += 1
        elif not mem is None and mem == sp[i] == sp[i + 1] and sp[i + 1] != sp[i + 2]:
            del sp[i]
            del sp[i]
            ans += 2
            mem = None
        elif sp[i] != sp[i + 1]:
            i += 1
    if not mem is None and mem == sp[i] == sp[i + 1] and i + 2 == len(sp):
        del sp[i]
        del sp[i]
        ans += 2
print(ans)