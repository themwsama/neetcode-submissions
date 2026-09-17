class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while right > left:
            while not s[right].isalnum() and right > left:
                right -= 1
            while not s[left].isalnum() and right > left:
                left += 1
            if right <= left:
                break
                
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1                   

        return True