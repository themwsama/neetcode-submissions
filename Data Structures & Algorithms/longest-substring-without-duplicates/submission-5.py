class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hasht = {}
        start = 0

        for i in range(len(s)):
            if (s[i] in hasht):
                start = max(start, hasht[s[i]] + 1)

            hasht[s[i]] = i
            longest = max(longest, i - start + 1)
            

        return longest