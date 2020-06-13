import collections


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    """
    146.LRU缓存机制 https://leetcode-cn.com/problems/lru-cache/
    """

    def __init__(self, capacity: int):
        self.cache = dict()
        # 添加伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            print(-1)
            return -1
        # 如果key存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        print(node.value)
        return node.value

    def put(self, key: int, value: int) -> int:
        if key not in self.cache:  # 如果key不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            self.cache[key] = node  # 添加进哈希表
            self.addToHead(node)  # 添加至双向链表的头部
            self.size += 1
            if self.size > self.capacity:  # 如果超出容量，删除双向链表的尾部节点
                removedNode = self.removeTail()
                self.cache.pop(removedNode.key)  # 删除哈希表中对应项
                self.size -= 1
        else:
            # 如果key存在，通过哈希定位，更新value，并移动到双向链表头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)        # 返回  1
    cache.put(3, 3)     # 该操作会使得关键字 2 作废
    cache.get(2)        # 返回 -1 (未找到)
    cache.put(4, 4)     # 该操作会使得关键字 1 作废
    cache.get(1)        # 返回 -1 (未找到)
    cache.get(3)        # 返回  3
    cache.get(4)        # 返回  4