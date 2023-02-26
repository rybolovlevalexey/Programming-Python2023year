class TreeNode:
    def __init__(self, name):
        self.name = name
        self.first = None
        self.second = None
        self.third = None


class Tree:
    def __init__(self, name):
        self.Head = TreeNode(name)


n = int(input())
prev = [None]
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    prev1 = set()
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
        prev1.add(i)
    if (i + 1) % 2 == 0:
        dp[i] += dp[i // 2]
        prev1.add((i + 1) // 2)
    if (i + 1) % 3 == 0:
        dp[i] += dp[i // 3]
        prev1.add((i + 1) // 3)
    prev.append(list(prev1))
