class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.head = (self.head - 1 + self.capacity) % self.capacity
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = (self.head + self.size) % self.capacity
        self.queue[tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        tail = (self.head + self.size - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
