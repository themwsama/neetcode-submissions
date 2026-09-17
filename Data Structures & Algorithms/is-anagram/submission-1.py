class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        for char in s:
            if char not in sCount:
                sCount[char] = 1
            else:
                sCount[char] += 1
        
        for char in t:
            if char not in tCount:
                tCount[char] = 1
            else:
                tCount[char] += 1


        if len(sCount) > len(tCount):
            for char, count in sCount.items():
                if char not in tCount:
                    return False
                if tCount[char] != count:
                    return False
        else:
            for char, count in tCount.items():
                if char not in sCount:
                    return False
                if sCount[char] != count:
                    return False
        

        return True
        
