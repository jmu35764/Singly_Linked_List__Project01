class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def append(self, value):
        new_node = node(value)
        
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self._head
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        self._count += 1

    def insert_after(self, existing_value, new_value):
        new_node = node(new_value)
        current = self._head

        while current.data is not existing_value:
            current = current.next

            if self._tail.data != existing_value and current is None:
                raise ValueError(f"Value {existing_value} not found in the list.")

        if current.data == self._tail.data:
            self._tail.next = new_node
            self._tail = new_node
        else:
            new_node.next = current.next
            current.next = new_node

    def remove(self, value):
        current = self._head
        previous = None

        while current and current.data != value:
            previous = current
            current = current.next

        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next

        if current == self._tail:
            self._tail = previous
            self._tail.next = None

        self._count -= 1       

    def contains(self, target):
        current = self._head

        while current is not None:
            if current.data == target:
                return True

        return False

    def is_empty(self):
        if self._head is None:
            return True

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        
        while current:
            yield current.data
            current = current.next


