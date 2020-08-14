class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Check is list is empty
        if self.head is None:
            return None

        # Check for list with length of 1
        if self.head.next_node is None:
            return self.head.value

        current = self.head.next_node # Start on second item
        prev_node = self.head

        while current is not None:
            future_current = current.next_node # Store the item that will be checked next loop
            current.set_next(prev_node)
            prev_node = current # Shift over one in the list
            current = future_current
        self.head = prev_node 
