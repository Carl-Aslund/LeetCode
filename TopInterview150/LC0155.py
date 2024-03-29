class MinStack:

    def __init__(self):
        # Use two stacks, one normal, and one for tracking min
        self.stack = []
        self.min_stack = [float('inf')]      

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]