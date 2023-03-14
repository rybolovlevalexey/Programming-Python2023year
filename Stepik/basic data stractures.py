n = int(input())
mn = set()
for i in range(n):
    st = input()
    mn.add(st)
m = int(input())
for j in range(m):
    st = input()
    flag = False
    for elem in mn:
        if elem == st or st.startswith(elem):
            flag = True
            break
    print("YES" if flag else "NO")