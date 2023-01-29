st = input()
sp = list(map(int, st.split()))
if "-" not in st:
    mn1 = None
    mn2 = None
    for elem in sp:
        if mn1 is None:
            mn1 = elem
        elif mn2 is None:
            mn2 = elem
        else:
            if elem < mn1:
                mn1, mn2 = elem, mn1
            elif mn1 < elem < mn2:
                mn2 = elem
    print(mn1 * mn2)
else:
    minus = None
    plus = None
    for elem in sp:
        if minus is None and elem < 0:
            minus = elem
        if plus is None and elem > 0:
            plus = elem
        else:
            if elem > plus and elem > 0:
                plus = elem
            if elem < minus and elem < 0:
                plus = elem
    print(plus * minus)
