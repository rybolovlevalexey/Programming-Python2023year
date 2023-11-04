n = int(input())
sp = map(int, input().split())
num = int(input())
count = 0
for elem in sp:
    if elem < num:
        count += 1
print(count, n - count, sep="\n")
