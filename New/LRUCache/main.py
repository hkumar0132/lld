'''
Requirements:

1. LRU Cache allows get and put operations
    - get (key, value): Get value for key and return -1 if it does not exist
    - put (key, value): Put key, value into cache
2. Eviction policy: If during put, cache reaches capacity, it will evict the LRU
3. A fixed capacity while initiating the cache
4. Multithreaded environment    

'''

Core Entities:
1. DoublyLinkedList
2. Node
3. LRUCache

Design:

exceptions/
class NodeNotFound(Exception):
    def __init__(self, message="Node not found"):
        super().__init__(message)
    
class Node:
    def __init__(self, key, value, prev: Node=None, next: Node=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
    def update_value(self, value):
        self.value = value


# 5, 1, 2, 3, 4 
class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
    
    def add_node_to_begining(self, node: Node) -> Node:
        if not node:
            raise NodeNotFound()
            
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def remove_node(self, node: Node):
        if not node:
            raise NodeNotFound()
        
        if node == self.head:
            self.remove_node_at_head()
            return
        elif node == self.tail:
            self.remove_node_at_tail()
            return
        
        node_to_be_deleted = node
        node.prev.next = node.next
        node.next.prev = node.prev    
        del node_to_be_deleted
        
    def remove_node_at_head(self):
        node_to_be_deleted = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del node_to_be_deleted
    
    def remove_node_at_tail(self):
        if not self.tail:
            raise NodeNotFound()
        
        node_to_be_deleted = self.tail
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None

        key = node_to_be_deleted.key
        del node_to_be_deleted
        return key    

    def move_to_begining(self, node: Node):
        self.remove_node(node)
        self.add_node_to_begining(node)
        
from threading import Lock    
class LRUCache:
    
    def __init__(self, capacity: int, doubly_list: DoublyLinkedList):
        self.capacity = capacity
        self.doubly_list = doubly_list
        self.cache = {} # key -> Node
        self.lock = Lock()
        
    def get(self, key):
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                self.doubly_list.move_to_begining(node)
                return node.value
            return -1
    
    def put(self, key, value):
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                self.doubly_list.move_to_begining(node)
                node.update_value(value)
            else:
                if len(self.cache) == self.capacity:
                    node_key = self.doubly_list.remove_node_at_tail()
                    del self.cache[node_key]
                
                node = Node(key, value)
                self.doubly_list.add_node_to_begining(node)
                self.cache[key] = node
    
controller/
def main():
    doubly_linked_list = DoublyLinkedList()
    cache = LRUCache(doubly_linked_list)
    
    cache.get("1")
    cache.put("1", { "a": 1, "b": 1 })

main()        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    