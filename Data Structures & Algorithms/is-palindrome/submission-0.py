class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_string = ""
        for char in s:
            if ((48 <= ord(char) <= 57) or (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)):
                alphanumeric_string += char.lower()

        leftp = 0
        rightp = len(alphanumeric_string)-1

        while (rightp > leftp):
            if (alphanumeric_string[rightp] == alphanumeric_string[leftp]):
                rightp -= 1
                leftp += 1
            else:
                return False
        return True
