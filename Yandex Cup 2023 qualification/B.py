n, m = map(int, input().split())
costs = list(map(int, input().split()))
if m == 0:
    print(0)
left, right = 0, n - 1
target = sorted(costs)[:m]
counter = {i: costs.count(i) for i in set(costs)}
for elem in target:
    counter[elem] -= 1
print(counter)
while True:
    le_val, ri_val = costs[left], costs[right]
    if counter[le_val] == 0 and counter[ri_val] == 0:
        break
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

print(counter)
print(right - left + 1)