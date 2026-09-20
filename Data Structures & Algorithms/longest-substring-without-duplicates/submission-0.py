class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        foundchar = set()
        first_index = 0
        i = 0
        while i < len(s):
        
            if s[i] in foundchar:
                foundchar.remove(s[first_index])
                first_index += 1
            else:
                foundchar.add(s[i])
                i+=1

            longest = max((i - first_index), longest)

        return longest