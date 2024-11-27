from points import Point

class Rectangle:
    '''Klasa reprezentująca prostokąty na płaszczyźnie.'''

    def __init__(self, x1, y1, x2, y2):
        if (x1 < x2) and (y1 < y2):
            self.p1 = Point(x1, y1)
            self.p2 = Point(x2, y2)
        else:
            raise ValueError('niepoprawne współrzędne wierzchołków')

    @classmethod
    def from_points(cls, points):
        return cls(points[0].x, points[0].y, points[1].x, points[1].y)

    def __str__(self):
        return '[{}, {}]'.format(self.p1, self.p2)

    def __repr__(self):
        return 'Rectangle({}, {}, {}, {})'.format(self.p1.x, self.p1.y,
                                                  self.p2.x, self.p2.y)

    def __eq__(self, other):
        return (self.p1 == other.p1) and (self.p2 == other.p2)

    def __ne__(self, other):
        return not self == other

    @property
    def center(self):
        return (self.p1 + self.p2) * 0.5

    @center.setter
    def center(self, point):
        x, y = self.center.x, self.center.y
        self.move(point[0]-x, point[1]-y)

    def area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))

    def move(self, x, y):
        '''Funkcja przesuwająca DANY prostokąt. Nie tworzy nowego prostokątu.'''
        self.p1 += Point(x, y)
        self.p2 += Point(x, y)

    def new_move(self, x, y):
        '''Funkcja tworząca NOWY prostokąt z przesuniętego danego prosokątu.'''
        import copy
        other = copy.deepcopy(self)
        other.p1 += Point(x, y)
        other.p2 += Point(x, y)
        return other

    def intersection(self, other):
        i_p1_x = max(self.p1.x, other.p1.x)
        i_p1_y = max(self.p1.y, other.p1.y)
        i_p2_x = min(self.p2.x, other.p2.x)
        i_p2_y = min(self.p2.y, other.p2.y)
        if (i_p1_x <= i_p2_x) and (i_p1_y <= i_p2_y):
            return Rectangle(i_p1_x, i_p1_y, i_p2_x, i_p2_y)
        else:
            raise ValueError('brak części wspólnej prostokątów')

    def cover(self, other):
        c_p1_x = min(self.p1.x, other.p1.x)
        c_p1_y = min(self.p1.y, other.p1.y)
        c_p2_x = max(self.p2.x, other.p2.x)
        c_p2_y = max(self.p2.y, other.p2.y)
        return Rectangle(c_p1_x, c_p1_y, c_p2_x, c_p2_y)

    def make4(self):
        p3 = self.center
        return (Rectangle(self.p1.x, p3.y, p3.x, self.p2.y),
                Rectangle(p3.x, p3.y, self.p2.x, self.p2.y),
                Rectangle(self.p1.x, self.p1.y, p3.x, p3.y),
                Rectangle(p3.x, self.p1.y, self.p2.y, p3.y))

    @property
    def top(self):
        return self.p2.y
    
    @property
    def left(self):
        return self.p1.x

    @property
    def bottom(self):
        return self.p1.y

    @property
    def right(self):
        return self.p2.x

    @property
    def width(self):
        return self.p2.x - self.p1.x

    @property
    def height(self):
        return self.p2.y - self.p1.y

    @property
    def bottomleft(self):
        return self.p1

    @property
    def bottomright(self):
        return Point(self.p2.x, self.p1.y)

    @property
    def topright(self):
        return self.p2

    @property
    def topleft(self):
        return Point(self.p1.x, self.p2.y)
