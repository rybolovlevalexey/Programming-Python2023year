st = input()
sp = list(map(int, st.split()))
mn1 = min(sp)
mx = max(sp)
sp.remove(mn1)
mn2 = min(sp)
if mn1 < 0:
    print(mn1 * mx)
else:
    print(mn1 * mn2)