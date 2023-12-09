n, k = map(int, input().split())
sp = list(map(int, input().split()))
nums_dict = dict()
ans = False
for i in range(n):
    num = sp[i]
    if num in nums_dict:
        if i - nums_dict[num] <= k:
            ans = True
            break
    nums_dict[num] = i
print("YES" if ans else "NO")