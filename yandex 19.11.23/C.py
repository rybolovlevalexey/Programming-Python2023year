n, m, q = map(int, input().split())
column_names: list[str] = input().split()
col_dict: dict[str, list[int]] = {key: list() for key in column_names}
bad_lines: set[int] = set()

for i in range(n):
    j = 0
    sp = list(map(int, input().split()))
    for key in column_names:
        col_dict[key] += [sp[j]]
        j += 1
for i in range(q):
    name, qk, value = input().split()
    line_ind = 0
    value = int(value)
    if len(bad_lines) == n:
        break
    if qk == ">":
        for elem in col_dict[name]:
            if elem <= value:
                bad_lines.add(line_ind)
            line_ind += 1
    else:
        for elem in col_dict[name]:
            if elem >= value:
                bad_lines.add(line_ind)
            line_ind += 1

if len(bad_lines) == n:
    print(0)
else:
    result = 0
    indexes = list(i for i in range(n) if i not in bad_lines)
    for column in col_dict.values():
        for i in indexes:
            result += column[i]
    print(result)
