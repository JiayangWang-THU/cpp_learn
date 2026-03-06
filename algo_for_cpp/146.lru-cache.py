#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_tail(self,node:Node)-> None:
        prev_last = self.tail.prev
        
        prev_last.next = node
        node.prev = prev_last

        node.next = self.tail
        self.tail.prev = node

    def _remove(self,node:Node)->None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_tail(self,node:Node)->None:
        self._remove(node)
        self._add_to_tail(node)

    def _pop_head(self)->Node:
        node = self.head.next
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_tail(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_tail(node)

            if len(self.cache) > self.capacity:
                removed = self._pop_head()
                del self.cache[removed.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

