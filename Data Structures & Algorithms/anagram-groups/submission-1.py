class Solution:

    # def isAnagram(s: str, t: str) -> bool:
    #     sAnagram = {}
    #     tAnagram = {}

    #     if len(s) != len(t):
    #         return False

    #     for i in range(len(s)):
    #         sAnagram[s[i]] = 1 + sAnagram.get(s[i], 0)
    #         tAnagram[t[i]] = 1 + tAnagram.get(t[i], 0)

    #     return sAnagram == tAnagram


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        elif len(strs) == 1:
            return [[strs[0]]]

        existAnagrams = {}

        for i in range(len(strs)):
            sortedString = "".join(sorted(strs[i]))
            if sortedString not in existAnagrams:
                existAnagrams[sortedString] = [strs[i]]
            else:
                existAnagrams[sortedString].append(strs[i])
        
        arrayYuh = []

        for _, listItem in existAnagrams.items():
            arrayYuh.append(listItem)

        return arrayYuh

                
            