ans = 0
n = int(input())
sp = list(map(int, input().split()))
st = ""
mem = None
cnt = 0
for i in range(len(sp) - 1):
    if sp[i] == sp[i + 1] and mem is None:
        mem = sp[i]
        cnt += 1
    elif sp[i] != sp[i + 1] and not mem is None:
        cnt += 1
        st += (str(mem) + str(cnt))
        mem = sp[i + 1]
        cnt = 1
    elif sp[i] != sp[i + 1] and mem is None:
        st += (str(mem) + '1')
        mem = sp[i + 1]
        cnt = 1
