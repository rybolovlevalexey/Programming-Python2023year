class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """

        flag1 = (length >= 10**4 or width >= 10**4 or height >= 10**4 or (width * height * length) >= 10**9)
        flag2 = mass >= 100
        if flag1 and flag2:
            return "Both"
        if not flag1 and not flag2:
            return "Neither"
        if flag1:
            return "Bulky"
        return "Heavy"

sl = Solution()

print(sl.categorizeBox(2593, 6432, 46, 412))