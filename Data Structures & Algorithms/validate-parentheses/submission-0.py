class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketmapping = { ')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if len(stack) > 0 and char in bracketmapping and bracketmapping[char] == stack[-1]:
                stack.pop()
            elif char in bracketmapping.values():
                stack.append(char)
            else:
                return False
        return len(stack) == 0


