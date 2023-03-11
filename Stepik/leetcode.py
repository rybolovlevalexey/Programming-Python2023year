from itertools import combinations


def threeSum(nums):
    indexes = combinations(range(0, len(nums)), 3)
    ans = list()
    for elem in indexes:
        line = sorted([nums[elem[0]], nums[elem[1]], nums[elem[2]]])
        if sum(line) == 0 and line not in ans:
            ans.append(line)
    return ans


sp = [12,13,-10,-15,4,5,-8,11,10,3,-11,4,-10,4,-7,9,1,8,-5,-1,-9,-4,3,-14,-11,14,0,-8,-6,-2,14,-9,-4,11,-8,-14,-7,-9,4,10,9,9,-1,7,-10,7,1,6,-8,12,12,-10,-7,0,-9,-3,-1,-1,-4,8,12,-13,6,-7,13,5,-14,13,12,6,8,-2,-8,-15,-10,-3,-1,7,10,7,-4,7,4,-4,14,3,0,-10,-13,11,5,6,13,-4,6,3,-13,8,1,6,-9,-14,-11,-10,8,-5,-6,-7,9,-11,7,12,3,-4,-7,-6,14,8,-1,8,-4,-11]
print(threeSum(sp))