from points import Point
import math

class Circle:
    '''Klasa reprezentująca okręgi na płaszczyźnie.'''

    def __init__(self, x, y, rad):
        if rad < 0:
            raise ValueError('ujemna wartość długości promienia')
        self.p = Point(x, y)
        self.rad = rad

    def __repr__(self):
        return 'Circle({}, {}, {})'.format(self.p.x, self.p.y, self.rad)

    def __eq__(self, other):
        return self.p == other.p and self.rad == other.rad

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * pow(self.rad, 2)

    def move(self, x, y):
        self.p += Point(x, y)

    def new_move(self, x, y):
        import copy
        other = copy.deepcopy(self)
        other.p += Point(x, y)
        return other

    def cover(self, other):
        # dystans pomiędzy środkami okręgów
        dist = math.sqrt((other.p.x-self.p.x) ** 2 + (other.p.y-self.p.y) ** 2)
        # jeśli pierwszy okrąg leży całkowicie wewnątrz drugiego
        if dist + self.rad <= other.rad:
            return Circle(other.p.x, other.p.y, other.rad)
        # jeśli drugi okrąg leży całkowicie wewnątrz pierwszego okręgu
        elif dist + other.rad <= self.rad:
            return Circle(self.p.x, self.p.y, self.rad)
        # jeśli nie, to okrąg pokrywający obydwa okręgu ma promień n_rad, a jego
        # środek (n_x, n_y) leży na linii łączącej środki obydwu okręgów
        else:
            n_rad = (dist + self.rad + other.rad) / 2
            # 0 < t <= 1
            t = (1/2) + (other.rad - self.rad) / (2*dist)
            n_x = (1-t) * self.p.x + t * other.p.x
            n_y = (1-t) * self.p.y + t * other.p.y
            return Circle(n_x, n_y, n_rad)
