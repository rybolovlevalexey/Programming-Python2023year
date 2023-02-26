n = int(input())
sp1 = set()
for i in range(n):
    sp1.add(input())
m = int(input())
cnt = 0
sp2 = set()
for j in range(m):
    st = input()
    if st in sp1:
        sp1.remove(st)
    else:
        sp2.add(st)
cnt = len(sp1) + len(sp2)
if cnt == 0:
    print("NO")
else:
    print(cnt)