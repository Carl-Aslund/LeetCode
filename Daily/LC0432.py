class Node:
    def __init__(self, key='', count=0):
        self.prev = None
        self.next = None
        self.count = count
        self.keys = {key}
    
    def insert(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node
        return node
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:
    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.root.next == self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            current = self.nodes[key]
            nextNode = current.next
            if nextNode == self.root or nextNode.count > current.count + 1:
                self.nodes[key] = current.insert(Node(key, current.count + 1))
            else:
                nextNode.keys.add(key)
                self.nodes[key] = nextNode
            current.keys.discard(key)
            if not current.keys:
                current.remove()

    def dec(self, key: str) -> None:
        current = self.nodes[key]
        if current.count == 1:
            del self.nodes[key]
        else:
            prevNode = current.prev
            if prevNode == self.root or prevNode.count < current.count - 1:
                self.nodes[key] = prevNode.insert(Node(key, current.count - 1))
            else:
                prevNode.keys.add(key)
                self.nodes[key] = prevNode
        current.keys.discard(key)
        if not current.keys:
            current.remove()

    def getMaxKey(self) -> str:
        if self.root.prev == self.root:
            return ""
        return next(iter(self.root.prev.keys))

    def getMinKey(self) -> str:
        if self.root.next == self.root:
            return ""
        return next(iter(self.root.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()