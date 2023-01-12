st = input().lower()
letters = dict()
for i in range(len(st)):
    elem = st[i]
    if not elem.isalpha():
        continue
    if elem in letters:
        letters[elem] += 1
    else:
        letters[elem] = 1
res = len(list(filter(lambda x: x % 2 == 1, letters.values())))
if res <= 1:
    print("YES")
else:
    print("NO")
