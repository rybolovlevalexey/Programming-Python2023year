n = int(input())
line_num = 1
while line_num <= n:
    n -= line_num
    line_num += 1
print(line_num - 1)