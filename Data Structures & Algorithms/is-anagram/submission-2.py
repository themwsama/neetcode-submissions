class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tdict, sdict = {}, {}

        for i in range(len(s)):
            tdict[t[i]] = 1 + tdict.get(t[i], 0)
            sdict[s[i]] = 1 + sdict.get(s[i], 0)

        return tdict == sdict


        
