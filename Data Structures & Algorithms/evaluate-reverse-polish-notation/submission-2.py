class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNumbers = []
        operations = {"+": True, "-": True, "/": True, "*": True}

        for t in tokens:
            if t in operations:
                numtwo = int(stackNumbers.pop())
                numone = int(stackNumbers.pop())
                value = numone
                if t == "+":
                    value += numtwo 
                elif t == "-":
                    value -= numtwo 
                elif t == "/":
                    if numtwo == 0:
                        value = 0
                    else:
                        value /= numtwo 
                elif t == "*":
                    value *= numtwo 
        
                stackNumbers.append(int(value))
            else:
                stackNumbers.append(int(t))

        return stackNumbers[-1]
