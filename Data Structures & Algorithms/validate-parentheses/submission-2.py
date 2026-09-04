class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 == 1):
            return False

        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif (s[i] == ")" and stack[len(stack)-1] == "(") or (s[i] == "}" and stack[len(stack)-1] == "{") or (s[i] == "]" and stack[len(stack)-1] == "["):
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0