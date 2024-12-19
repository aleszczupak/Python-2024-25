class SingleList:
    '''Klasa reprezentująca całą listę jednokierunkową.'''

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0
        #return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None # czyszczenie łącza
        self.length -= 1
        return node

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __next__(self):
        if self.current:
            node = self.current
            self.current = self.current.next
            return node.data
        else:
            raise StopIteration

    # nowe metody:

    def remove_tail(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while node.next != self.tail:
                node = node.next
            self.tail = node
            node.next = None
        self.length -= 1
        return node

    def join(self, other):
        node = other.head
        while node:
            self.insert_tail(node)
            node = node.next
            other.remove_head()
        return node

    def clear(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while node is not None:
                node = node.next
                self.remove_head()
        return node

    def search(self, data):
        node = self.head
        position = 0
        while node:
            if node.data == data:
                return node
            node = node.next
            position += 1
        return None

    def find_min(self):
        if self.is_empty():
            return None
        min_node = self.head
        node = self.head
        while node:
            if node.data < min_node.data:
                min_node = node
            node = node.next
        return min_node

    def find_max(self):
        if self.is_empty():
            return None
        max_node = self.head
        node = self.head
        while node:
            if node.data > max_node.data:
                max_node = node
            node = node.next
        return max_node

    def reverse(self):
        prev_node = None
        node = self.head
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        self.head = prev_node
