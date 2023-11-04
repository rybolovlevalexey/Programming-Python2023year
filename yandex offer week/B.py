n, m = map(int, input().split())
first, second = min(n, m), max(n, m)
length = len(str(second - 1))
count = 0

for i in range(first):
    time1 = str(i)
    time1 = "0" * (length - len(time1)) + time1
    time2 = int(time1[::-1])
    if time2 < second:
        count += 1
print(count)