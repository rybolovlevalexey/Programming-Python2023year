n = int(input())
arrays = list()
int(input())
arrays.append(input().split())
for i in range(n - 1):
    k = int(input())
    sp = input().split()
    if sp < arrays[0]:
        arrays.insert(0, sp)
    else:
        for j in range(len(arrays)):
            if arrays[j] < sp and (j + 1 == len(arrays) or sp < arrays[j + 1]):
                arrays.insert(j + 1, sp)
print(arrays)