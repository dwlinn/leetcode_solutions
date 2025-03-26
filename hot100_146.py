class DlinkedNode:
    def __int__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DlinkedNode(key, value)
            self.add(node)
            self.cache[key] = value
            self.size += 1
            if self.size > self.capacity:
                del self.cache[self.tail.prev.key]
                self.remove(self.tail.prev)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.remove(node)
        self.add(node)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)
