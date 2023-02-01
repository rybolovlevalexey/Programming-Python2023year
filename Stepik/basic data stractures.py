n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for elem in a:
    flag = True
    for el in b:
        if elem == el:
            flag = False
            break
    if flag:
        print(elem, end=' ')
