from models.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    
    def get_new_node(self, key):
        return Node(key)
        
    def detach_node_with_key(self, key):
        node = self.head
        while node:
            if node.key == key:
                self._detach_node(node)
                return node
            node = node.next
        
    def _detach_node(self, node):
        if not node:
            return
        temp = node.prev
        # self.print_list()
        
        if node.prev:
            node.prev.next = node.next
            # self.print_list()
        else:
            self.move_head()
            # self.print_list()
            return
        if node.next:
            node.next.prev = temp
        # self.print_list()
        
    def attach_at_tail(self, node):
        # print(f"ATTACHING NODE AT TAIL: {node}")
        if not self.head:
            self.head = node
            # print("NOT SELF HEAD")
            # self.print_list()
            return
        
        trav = self.head
        while trav and trav.next:
            trav = trav.next

        trav.next = node
        node.prev = trav
        node.next = None
        # self.print_list()

    def move_head(self):
        prev_head = self.head
        key_at_head = prev_head.key
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        # self.print_list()
        del prev_head
        return key_at_head
    
    def print_list(self):
        node = self.head
        while node:
            print(node.key, end="--")
            node = node.next
        print()