def func(x):
    if x <= 9:
        return x
    return func(sum(map(int, list(str(x)))))


n = int(input())
for i in range(n):
    first, second = map(int, input().split())
    num = first
    for j in range(first + 1, second + 1):
        num *= j
    print(func(num))
