n = int(input())
sp = list()
cnt = 0
prev = None
for i in range(n):
    if i == 0:
        prev = int(input())
    else:
        x = int(input())
        cnt += min(x, prev)
        prev = x
print(cnt)