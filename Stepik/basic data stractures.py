n = int(input())
sp1 = list(map(int, input().split()))
m = int(input())
sp2 = list(map(int, input().split()))
ans = list()
i = 0
j = 0
while i < n and j < m:
    if sp1[i] < sp2[j]:
        ans.append(sp1[i])
        print(sp1[i], end=" ")
        i += 1
    elif sp1[i] == sp2[j]:
        ans.append(sp1[i])
        ans.append(sp2[j])
        print(sp1[i], end=" ")
        print(sp2[j], end=" ")
        i += 1
        j += 1
    else:
        ans.append(sp2[j])
        print(sp2[j], end=" ")
        j += 1
while i < n:
    print(sp1[i], end=" ")
    i += 1
while j < m:
    print(sp2[j], end=" ")
    j += 1
