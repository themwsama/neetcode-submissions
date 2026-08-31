class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasht = {}
        anagrams = []

        if (len(strs) == 1):
            return [[strs[0]]]

        for s in strs:
            item = "".join(sorted(s))
            if item in hasht:
                anagrams[hasht[item]].append(s)
            else:
                hasht[item] = len(anagrams)
                anagrams.append([s])

        return anagrams