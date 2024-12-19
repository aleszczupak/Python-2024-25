class Node:
    '''Klasa reprezentująca węzeł listy dwukierunkowej.'''

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not self == other
