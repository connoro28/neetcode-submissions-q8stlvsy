class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.right = Node()
        self.left = Node()
        self.capacity = capacity
        self.cache = {}
        self.left.next = self.right
        self.right.prev = self.left

    def _insert(self, node):
        last = self.right.prev
        last.next = node
        self.right.prev = node
        node.prev = last
        node.next = self.right

    def _remove(self, node):
        last = node.prev
        lead = node.next
        last.next = lead
        lead.prev = last

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._remove(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

        
