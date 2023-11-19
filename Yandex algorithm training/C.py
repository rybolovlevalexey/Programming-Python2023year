n = int(input())
sp1 = input().split()
m = int(input())
sp2 = input().split()
i, j = 0, 0
while i < n or j < m:
    if j == m or sp1[i] < sp2[j]:
        print(sp1[i], end=" ")
        i += 1
    else:
        print(sp2[j], end=" ")
        j += 1
