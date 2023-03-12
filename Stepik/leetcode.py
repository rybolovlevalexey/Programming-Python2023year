class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = list()
        three, five, num = 1, 1, 1
        while num <= n:
            if five == 5 and three == 3:
                ans.append("FizzBuzz")
                five, three = 1, 1
            elif three == 3:
                ans.append("Fizz")
                three = 1
                five += 1
            elif five == 5:
                ans.append("Buzz")
                five = 1
                three += 1
            else:
                ans.append(str(num))
                three += 1
                five += 1
            num += 1
        return ans