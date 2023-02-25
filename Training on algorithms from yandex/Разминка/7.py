class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __lt__(self, other):
        return (self.h < other.h) or (self.h == other.h and self.m < other.m) or \
               (self.h == other.h and self.m == other.m and self.s < other.s)


first = list(map(int, input().split(":")))
second = list(map(int, input().split(":")))
third = list(map(int, input().split(":")))
A = first[0] * 3600 + first[1] * 60 + first[2]
if Time(*first) < Time(*third):
    C = third[0] * 3600 + third[1] * 60 + third[2]
else:
    C = (third[0] + 24) * 3600 + third[1] * 60 + third[2]
delay = (C - A) / 2
if delay == int(delay):
    delay = int(delay)
else:
    ost = float("0" + str(delay).split(".")[1])
    delay = int(delay)
    if not (delay < 1/2):
        delay += 1
B = second[0] * 3600 + second[1] * 60 + second[2]
B += delay
ans = list()
ans.append(B // 3600)
ans.append((B - 3600 * ans[0]) // 60)
ans.append(B - 3600 * ans[0] - 60 * ans[1])
ans[0] = ans[0] % 24
for i in range(len(ans)):
    if len(str(ans[i])) == 1:
        ans[i] = "0" + str(ans[i])
ans = ":".join(map(str, ans)).strip()
print(ans)