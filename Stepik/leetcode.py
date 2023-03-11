import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.og_nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.og_nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        ans = self.og_nums[::-1]
        for i in range(len(ans) * 3):
            ind1 = random.randint(0, len(ans))
            ind2 = random.randint(0, len(ans))
            if ind1 == ind2:
                continue
            ans[ind1], ans[ind2] = ans[ind2], ans[ind1]
        return ans


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2, param_1)