n = int(input())
sp1 = list(map(int, input().split()))
m = int(input())
sp2 = list(map(int, input().split()))
i = 0
j = 0
while i < n and j < m:
    if sp1[i] == sp2[j]:
        print(sp1[i], end=" ")
        i += 1
        j += 1
    else:
        if sp1[i] > sp2[j]:
            while j < m and sp1[i] > sp2[j]:
                j += 1
        else:
            while i < n and sp1[i] < sp2[j]:
                i += 1
