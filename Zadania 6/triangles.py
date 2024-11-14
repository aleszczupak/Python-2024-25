from points import Point
from itertools import permutations
import math

class Triangle:
    '''Klasa reprezentująca trójkąt na płaszczyźnie.'''

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
            raise ValueError('punkty współliniowe')
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

    def __str__(self):
        return '[' + str(self.p1) + ', ' + str(self.p2) + ', ' + str(self.p3) + ']'
    
    def __repr__(self):
        return 'Triangle(' + str(self.p1.x) + ', ' + str(self.p1.y) + ', ' +\
               str(self.p2.x) + ', ' + str(self.p2.y) + ', ' + str(self.p3.x) +\
               ', ' + str(self.p3.y) + ')'

    def __eq__(self, other):
        perms = list(permutations([other.p1, other.p2, other.p3]))
        triangle = (self.p1, self.p2, self.p3)
        cases = [triangle == perm for perm in perms]
        return True if any(cases) else False

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.p1.x + self.p2.x + self.p3.x) / 3,
                     (self.p1.y + self.p2.y + self.p3.y) / 3)

    def area(self):
        a = math.sqrt((self.p2.x - self.p1.x) ** 2 +\
                      (self.p2.y - self.p1.y) ** 2)
        b = math.sqrt((self.p3.x - self.p2.x) ** 2 +\
                      (self.p3.y - self.p2.y) ** 2)
        c = math.sqrt((self.p1.x - self.p3.x) ** 2 +\
                      (self.p1.y - self.p3.y) ** 2)
        p = (a + b + c) / 2
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

    def move(self, x, y):
        self.p1 += Point(x, y)
        self.p2 += Point(x, y)
        self.p3 += Point(x, y)

    def new_move(self, x, y):
        import copy
        other = copy.deepcopy(self)
        other.p1 += Point(x, y)
        other.p2 += Point(x, y)
        other.p3 += Point(x, y)
        return other
