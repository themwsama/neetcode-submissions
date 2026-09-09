class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for tok in tokens:
            if tok in ["+", "-", "/", "*"]:
                b = nums.pop()
                a = nums.pop()

                if tok == "+":
                    nums.append(a + b)
                elif tok == "-":
                    nums.append(a - b)
                elif tok == "*":
                    nums.append(a * b)
                else:
                    nums.append(int(a / b))

            else:
                nums.append(int(tok))
            
        return nums[0]