n = int(input())  # порты
gadg = m = int(input())  # гаджеты
c2 = int(input())  # на 2 порта
c5 = int(input())  # на 5 портов
cnt1, cnt2, cnt5 = n, 0, 0
if m <= n:
    print(0)
else:
    while m > 5 * n:
        cnt5 += n
        m -= 5 * n

    while cnt1 >= 1:
        if m % 5 == 0:
            cnt5 = m // 5
            cnt1 -= cnt5
            m = 0
        elif m % 5 == 1:
            cnt5 = m // 5
            cnt1 -= (cnt5 + 1)
            m = 0
        elif m % 5 == 2:
            cnt5 = m // 5
            cnt2 += 1
            cnt1 -= (cnt5 + 1)
            m = 0
        elif m % 5 == 3:
            cnt5 = m // 5
            cnt1 -= cnt5
            if cnt1 == 1:
                cnt1 -= 1
                cnt2 += 2
            else:
                cnt1 -= 2
                cnt2 += 1
            m = 0
        elif m % 5 == 4:
            cnt5 = m // 5
            cnt1 -= cnt5
            if cnt1 == 1:
                cnt1 -= 1
                if 3 * c2 < c5:
                    cnt2 += 3
                else:
                    cnt5 += 1
            else:
                if 2 * c2 < c5:
                    cnt1 -= 2
                    cnt2 += 2
                else:
                    cnt1 -= 1
                    cnt5 += 1
            m = 0
        if cnt1 == 1 and cnt2 > 0:
            cnt2 -= 1
            cnt1 -= 1
            break
        elif cnt1 > 1:
            m += 5
            cnt5 -= 1
            cnt1 += 1

    cost = c2 * cnt2 + c5 * cnt5
    print(cost)