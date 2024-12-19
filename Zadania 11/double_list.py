class DoubleList:
    '''Klasa reprezentująca całą listę dwukierunkową.'''

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        # pusta lista
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None
            node.next = None
            self.length -= 1
            return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        elif self.head is self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
            self.length -= 1
            return node

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __reversed__(self):
        node = self.tail
        while node:
            yield node.data
            node = node.prev

    # nowe metody:

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

    def remove_index(self, index):
        if self.length <= index:
            raise ValueError('niepoprawny indeks')
        if index == 0:
            self.remove_head()
            return
        if index == self.length - 1:
            self.remove_tail()
            return
        temp = self.head
        for i in range(index):
            temp = temp.next
        prevnode = temp.prev
        nextnode = temp.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        self.length -= 1
        #del temp

    def remove(self, delnode):
        counter = 0
        node = self.head
        if self.head.data == delnode:
            self.remove_head()
            return
        if self.tail.data == delnode:
            self.remove_tail()
            return
        while node:
            counter += 1
            if node.data == delnode:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                break
            node = node.next
        if counter == self.length:
            raise ValueError('brak takiego węzła')
        else:
            self.length -= 1
