k = int(input())
st = input()
ans = tuple()

for letter in set(st):
    end = 0
    cnt = k
    for beg in range(len(st)):
        if st[beg] != letter and cnt > 0:
            cnt -= 1
        if beg != 0 and st[beg - 1] != letter:
            cnt += 1

        while end < len(st):
            if end <= beg:
                pass
            else:
                if st[end] == letter and cnt == 0:
                    dl = end - beg + 1
                    if len(ans) == 0 or dl > ans[0]:
                        ans = (dl, st[beg: end + 1])
                elif st[end] != letter and cnt == 0:
                    break
                elif st[end] != letter and cnt > 0:
                    cnt -= 1
                    dl = end - beg + 1
                    if len(ans) == 0 or dl > ans[0]:
                        ans = (dl, st[beg: end + 1])
                elif st[end] == letter and cnt > 0:
                    # цикл продолжается, если буква совпала
                    dl = end - beg + 1
                    if len(ans) == 0 or dl > ans[0]:
                        ans = (dl, st[beg: end + 1])
            end += 1
print(ans[0])