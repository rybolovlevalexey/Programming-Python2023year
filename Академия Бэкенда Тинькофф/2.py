m = int(input())
sp = list()
for i in range(m):
    st = input()
    if st.startswith("1"):
        sp.append(st.split()[1])
    elif st.startswith("2"):
        new_sp = list()
        for j in range(len(sp)):
            elem = sp[j]
            new_sp.append(elem)
            new_sp.append(elem)
        sp = new_sp.copy()
    else:
        elem = sp.pop(0)
        print(elem)