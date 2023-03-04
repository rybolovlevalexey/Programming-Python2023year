k = int(input())
st = input()
if k == 0:
    dl = mx_dl = 0
    last = None
    for elem in st:
        if last is None:
            last = elem
            dl += 1
            if dl > mx_dl:
                mx_dl = dl
        elif last == elem:
            dl += 1
            if dl > mx_dl:
                mx_dl = dl
        elif last != elem:
            last = elem
            dl = 1
    print(dl)
else:
    ans = None
    for let in range(ord("a"), ord("z") + 1):
        left = 0
        right = 1
        elem = chr(let)
        cnt = k
        mx_dl = right - left + 1
        if st[left] != elem and st[right] != elem and cnt >= 2:  # дописать
            cnt -= 2
            right += 1
            while left < len(st):
                while right < len(st):
                    if st[right] != elem and cnt == 0:
                        break
                    dl = right - left + 1
                    if st[right] == elem:
                        if dl > mx_dl:
                            mx_dl = dl
                    elif st[right] != elem and cnt > 0:
                        cnt -= 1
                        if dl > mx_dl:
                            mx_dl = dl
                    right += 1
                left += 1
                if st[left - 1] != elem:
                    cnt += 1
        elif st[left] != elem and st[right] != elem and cnt < 2:
            while st[left] != elem and st[right] != elem and right < len(st):
                left += 1
                right += 1
            if right + 1 == len(st):
                mx_dl = 1  # выход
            else:
                if (st[left] != elem and st[right] == elem) or \
                        (st[left] == elem and st[right] != elem):
                    cnt -= 1
                    right += 1
                    while left < len(st):
                        while right < len(st):
                            if st[right] != elem and cnt == 0:
                                break
                            dl = right - left + 1
                            if st[right] == elem:
                                if dl > mx_dl:
                                    mx_dl = dl
                            elif st[right] != elem and cnt > 0:
                                cnt -= 1
                                if dl > mx_dl:
                                    mx_dl = dl
                            right += 1
                        left += 1
                        if st[left - 1] != elem:
                            cnt += 1

        elif (st[left] != elem and st[right] == elem) or \
                (st[left] == elem and st[right] != elem):  # дописать
            cnt -= 1
            right += 1
            while left < len(st):
                while right < len(st):
                    if st[right] != elem and cnt == 0:
                        break
                    dl = right - left + 1
                    if st[right] == elem:
                        if dl > mx_dl:
                            mx_dl = dl
                    elif st[right] != elem and cnt > 0:
                        cnt -= 1
                        if dl > mx_dl:
                            mx_dl = dl
                    right += 1
                left += 1
                if st[left - 1] != elem:
                    cnt += 1

        elif st[right] == st[left] == elem:
            # цикл работает корректно
            while left < len(st):
                while right < len(st):
                    if st[right] != elem and cnt == 0:
                        break
                    dl = right - left + 1
                    if st[right] == elem:
                        if dl > mx_dl:
                            mx_dl = dl
                    elif st[right] != elem and cnt > 0:
                        cnt -= 1
                        if dl > mx_dl:
                            mx_dl = dl
                    right += 1
                left += 1
                if st[left - 1] != elem:
                    cnt += 1

        if ans is None or ans < mx_dl:
            ans = mx_dl
    print(ans)
