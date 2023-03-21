n = int(input())
goblins = list()
for i in range(n):
    st = input()
    if st == "-":
        print(goblins[0])
        del goblins[0]
    else:
        st = st.split()
        if st[0] == "+":
            goblins.append(st[1])
        else:
            goblins = goblins[:len(goblins) // 2 + len(goblins) % 2] + [st[1]]\
                      + goblins[len(goblins) // 2 + len(goblins) % 2:]
