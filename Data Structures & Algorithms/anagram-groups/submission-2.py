class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]

        recorded_anagrams = {}

        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in recorded_anagrams:
                recorded_anagrams[sorted_word].append(strs[i])
            else:
                recorded_anagrams[sorted_word] = [strs[i]]
     
        return list(recorded_anagrams.values())

        
                
            