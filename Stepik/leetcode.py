class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = dict()
        for elem in magazine:
            if elem not in letters:
                letters[elem] = 1
            else:
                letters[elem] += 1
        for elem in ransomNote:
            if elem not in letters or letters[elem] == 0:
                return False
            letters[elem] -= 1
        return True
