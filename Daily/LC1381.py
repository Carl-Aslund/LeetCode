class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.add = [0] * maxSize
        self.currentSize = 0

    def push(self, x: int) -> None:
        if self.currentSize < len(self.stack):
            self.stack[self.currentSize] = x
            self.currentSize += 1

    def pop(self) -> int:
        if self.currentSize <= 0:
            return -1
        self.currentSize -= 1
        result = self.stack[self.currentSize] + self.add[self.currentSize]
        if self.currentSize > 0:
            self.add[self.currentSize - 1] += self.add[self.currentSize]
        self.add[self.currentSize] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        limit = min(k, self.currentSize) - 1
        if limit >= 0:
            self.add[limit] += val
