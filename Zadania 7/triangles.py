from points import Point
#from itertools import permutations

class Triangle:
    '''Klasa reprezentująca trójkąt na płaszczyźnie.'''

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
            self.p1 = Point(x1, y1)
            self.p2 = Point(x2, y2)
            self.p3 = Point(x3, y3)
        else:
            raise ValueError('punkty współliniowe')

    def __str__(self):
        return '[{}, {}, {}]'.format(self.p1, self.p2, self.p3)
    
    def __repr__(self):
        return 'Triangle({}, {}, {}, {}, {}, {})'.format(self.p1.x, self.p1.y,
                                                         self.p2.x, self.p2.y,
                                                         self.p3.x, self.p3.y)

    def __eq__(self, other):
        return {self.p1, self.p2, self.p3} == {other.p1, other.p2, other.p3}

    def __ne__(self, other):
        return not self == other

    def center(self):
        #return Point((self.p1.x + self.p2.x + self.p3.x) / 3,
                     #(self.p1.y + self.p2.y + self.p3.y) / 3)
        return (self.p1 + self.p2 + self.p3) / 3.0
    
    def area(self):
        return abs(((self.p1.x * (self.p2.y-self.p3.y) +\
                     self.p2.x * (self.p3.y-self.p1.y) +\
                     self.p3.x * (self.p1.y-self.p2.y))) / 2)

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

    def make4(self):
        p4_x = (self.p1.x + self.p2.x) / 2
        p4_y = (self.p1.y + self.p2.y) / 2
        p5_x = (self.p2.x + self.p3.x) / 2
        p5_y = (self.p2.y + self.p3.y) / 2
        p6_x = (self.p1.x + self.p3.x) / 2
        p6_y = (self.p1.y + self.p3.y) / 2
        return (Triangle(self.p1.x, self.p1.y, p4_x, p4_y, p6_x, p6_y),
                Triangle(p4_x, p4_y, p5_x, p5_y, p6_x, p6_y),
                Triangle(p6_x, p6_y, p5_x, p5_y, self.p3.x, self.p3.y),
                Triangle(p4_x, p4_y, self.p2.x, self.p2.y, p5_x, p5_y))
