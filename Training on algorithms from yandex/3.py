n = int(input())
diego = set(sorted(map(int, input().split())))
k = int(input())
collectors = list(map(int, input().split()))
for p in collectors:
    ans = 0
    for elem in diego:
        if elem >= p:
            break
        ans += 1
    print(ans)
