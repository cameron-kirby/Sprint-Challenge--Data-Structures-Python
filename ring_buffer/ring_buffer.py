from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Add elements until capacity is equal to current
        if self.current < self.capacity: 
            self.storage.add_to_tail(item)
            self.current += 1
        elif self.current == self.capacity:
            self.storage.delete(self.storage.head)
            self.storage.add_to_head(item)
            self.current += 1
        else:
            current = self.storage.head # get the head
            for i in range(self.current - self.capacity): # Runs through buffer
                if current.next is not None: # Checks for end of buffer
                    current = current.next # grabs the next node
            current.insert_before(item)
            current.delete()
            self.current += 1
            if self.current == (self.capacity * 2):
                self.current = self.capacity

    def get(self):
        list_buffer_contents = []

        # Start at head
        current = self.storage.head
        while current is not None: # Check for end
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents