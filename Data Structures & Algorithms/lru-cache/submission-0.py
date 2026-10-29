class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.data = {}

        # dummy nodes
        self.left = Node()   # LRU 쪽
        self.right = Node()  # MRU 쪽

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        node = self.data[key]

        # 최근에 사용했으므로 맨 오른쪽으로 이동
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]

            node.value = value

            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.data[key] = node

            self.insert(node)
            self.count += 1

            if self.count > self.capacity:
                # 가장 오래 사용되지 않은 노드
                lru = self.left.next

                self.remove(lru)
                del self.data[lru.key]

                self.count -= 1