n = int(input())
sp = list(map(int, input().split()))
numbers = dict()
for elem in sp:
    if elem not in numbers:
        numbers[elem] = 1
    else:
        numbers[elem] += 1
for key, value in numbers.items():
    if value == 1:
        print(key, end=" ")
