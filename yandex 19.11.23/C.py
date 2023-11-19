n, m, q = map(int, input().split())
column_names: list[str] = input().split()
col_dict: dict[str, list[int]] = {key: list() for key in column_names}
# bad_lines: set[int] = set()
lines_sum = dict()
result = 0
minus_lines = set()
for i in range(n):
    j = 0
    sp = list(map(int, input().split()))
    for key in column_names:
        col_dict[key] += [sp[j]]
        j += 1
    summa = sum(sp)
    lines_sum[i] = summa
    result += summa
for i in range(q):
    name, qk, value = input().split()
    line_ind = 0
    value = int(value)
    if len(minus_lines) == n:
        break
    if qk == ">":
        for elem in col_dict[name]:
            if elem <= value:
                if line_ind not in minus_lines:
                    minus_lines.add(line_ind)
                    result -= lines_sum[line_ind]
            line_ind += 1
    else:
        for elem in col_dict[name]:
            if elem >= value:
                if line_ind not in minus_lines:
                    minus_lines.add(line_ind)
                    result -= lines_sum[line_ind]
            line_ind += 1
print(result)
