class MinStack:

    def __init__(self):
        self.values = []
        self.min_stack = []  # Tracks the minimum value at each state

    def push(self, val: int) -> None:
        self.values.append(val)
        # If min_stack is empty or val is smaller/equal to current min, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.values:
            # If the value being popped is the current minimum, pop it from min_stack too
            if self.values[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
