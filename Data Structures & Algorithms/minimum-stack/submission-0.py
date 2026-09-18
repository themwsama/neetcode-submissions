class MinStack:

    def __init__(self):
        self.array = []
        self.minStack = []
        self.min = None

    def push(self, val: int) -> None:
        self.array.append(val)
        value = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(value)

    def pop(self) -> None:
        self.array.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.array) == 0:
            return None
        return self.array[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

        
