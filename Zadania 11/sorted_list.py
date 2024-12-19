from single_node import Node

class SortedList:
    '''Klasa reprezentująca posortowaną malejąco listę jednokierunkową.'''
    
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

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
        
    def insert(self, newnode):
        node = None
        if (self.head is None or self.head.data <= newnode.data):
            newnode.next = self.head
            self.head = newnode
        else:
            node = self.head
            while (node.next is not None and node.next.data > newnode.data):
                node = node.next
            newnode.next = node.next
            node.next = newnode
        self.length += 1
        return self.head   

    def remove(self):
        # zwraca node z elementem największym, czyli head
        if self.is_empty():
            raise ValueError('pusta lista')
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    '''def merge(self, other):
        node = other.head
        while node:
            self.insert(node)
            node = node.next
            other.remove()
        return node'''

    def merge(self, other):
        temp = Node()
        node1 = self.head
        node2 = other.head
        while node1 is not None and node2 is not None:
            if node1.data > node2.data:
                temp.next = node1
                node1 = node1.next
                self.length += 1
            else:
                temp.next = node2
                node2 = node2.next
                other.remove()
            temp = temp.next
        if node1 is not None:
            temp.next = node1
            self.length += 1
        else:
            temp.next = node2
        return node1

    def clear(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while node is not None:
                node = node.next
                self.remove()
        return node
