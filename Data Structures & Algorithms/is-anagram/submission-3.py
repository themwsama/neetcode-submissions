class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in sCount:
                sCount[char] += 1
            else:
                sCount[char] = 1

        for char in t:
            if char in tCount:
                tCount[char] += 1
            else:
                tCount[char] = 1

       
        return sCount == tCount