st = input()
sp = list(map(int, st.split()))
ans = None
start = 0
end = start + 1
while end < len(sp):
    res = sp[start] * sp[end]
    if ans is None or res < ans:
        ans = res
    end += 1
    if end == len(sp):
        start += 1
        end = start + 1
print(ans)