n = int(input())
print(sum(filter(lambda x: x % 2 == 0 and x > 0, map(int, input().split()))))