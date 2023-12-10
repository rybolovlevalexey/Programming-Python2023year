n = int(input())
nums = sorted(map(int, input().split()))
left, right = 0, 0
count = 0
for i in range(n):
    while left < n and nums[left] <= nums[i] * 0.5 + 7:
        left += 1
    while right < n and nums[right] <= nums[i]:
        right += 1
    if right != left:
        count += right - left - 1
print(count)