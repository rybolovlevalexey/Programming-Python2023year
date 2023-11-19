n, m, q = map(int, input().split())
column_names: list[str] = input().split()
col_dict: dict[str, list[int]] = {key: list() for key in column_names}
lines_sum = dict()
result = 0
minus_lines = set()
actions = dict()
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
    value = int(value)
    if name not in actions:
        actions[name] = dict()

    if qk not in actions[name]:
        actions[name][qk] = value
    else:
        if qk == ">":
            actions[name][qk] = max(value, actions[name][qk])
        else:
            actions[name][qk] = min(value, actions[name][qk])

for name, acts in actions.items():
    if len(minus_lines) == n:
        break
    upper = acts.get("<", None)
    down = acts.get(">", None)
    line_ind = 0
    if upper is None:
        for elem in col_dict[name]:
            if elem <= down and line_ind not in minus_lines:
                minus_lines.add(line_ind)
                result -= lines_sum[line_ind]
            line_ind += 1
    elif down is None:
        for elem in col_dict[name]:
            if elem >= upper and line_ind not in minus_lines:
                minus_lines.add(line_ind)
                result -= lines_sum[line_ind]
            line_ind += 1
    else:
        for elem in col_dict[name]:
            if (elem >= upper or elem <= down) and line_ind not in minus_lines:
                minus_lines.add(line_ind)
                result -= lines_sum[line_ind]
            line_ind += 1
print(result)
