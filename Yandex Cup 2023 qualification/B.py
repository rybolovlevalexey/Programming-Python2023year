n, m = map(int, input().split())
costs = list(map(int, input().split()))
left, right = 0, n - 1
target = sorted(costs)[:m]
counter = {i: costs.count(i) for i in set(costs)}
for elem in target:
    counter[elem] -= 1
le_val, ri_val = costs[left], costs[right]
while counter[le_val] != 0 or counter[ri_val] != 0:
    le_val, ri_val = costs[left], costs[right]
    if counter[le_val] > 0:
        left += 1
        counter[le_val] -= 1
    if left == right:
        break
    if counter[ri_val] > 0:
        right -= 1
        counter[ri_val] -= 1
    if left == right:
        break

print(right - left + 1)
