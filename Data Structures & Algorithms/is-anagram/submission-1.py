class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

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

        if len(sCount) > len(tCount):
            for sCountKey in sCount:
                if not (sCountKey in tCount):
                    return False
                if sCount[sCountKey] != tCount[sCountKey]:
                    return False
        else:
            for tCountKey in tCount:
                if not (tCountKey in sCount):
                    return False
                if sCount[tCountKey] != tCount[tCountKey]:
                    return False
        return True