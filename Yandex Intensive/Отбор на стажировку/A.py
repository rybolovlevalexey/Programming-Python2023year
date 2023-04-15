n = int(input())
klavishy = dict()
klavishy_input = input().split()
ryad_input = input().split()
for key, value in zip(klavishy_input, ryad_input):
    klavishy[key] = int(value)
k = int(input())
st = input().split()
ans = 0
for i in range(1, k):
    if klavishy[st[i - 1]] != klavishy[st[i]]:
        ans += 1
print(ans)