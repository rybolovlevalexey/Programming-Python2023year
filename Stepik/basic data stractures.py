ans = set()
for i in range(int(input())):
    mn = set()
    for j in range(int(input())):
        mn.add(input())
    if i == 0:
        ans = mn.copy()
    else:
        ans = ans & mn
print(len(ans))