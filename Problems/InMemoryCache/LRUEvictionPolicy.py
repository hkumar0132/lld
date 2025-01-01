from models.EvictionPolicy import EvictionPolicy
from LinkedList import LinkedList


class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.linked_list = LinkedList()
        
    def key_accessed(self, key):
        node = self.linked_list.detach_node_with_key(key)
        if not node:
            node = self.linked_list.get_new_node(key)
        self.linked_list.attach_at_tail(node)
        
        self.linked_list.print_list()
    
    def evict_key(self, key):
        self.linked_list.detach_node_with_key(key)
        
        self.linked_list.print_list()
    
    def remove_most_recent_used(self):
        result = self.linked_list.move_head()
        # self.linked_list.print_list()
        return result