from points import Point
import math

class Circle:
    '''Klasa reprezentująca okręgi na płaszczyźnie.'''

    def __init__(self, x, y, rad):
        if rad < 0:
            raise ValueError('ujemny promień')
        self.p = Point(x, y)
        self.rad = rad

    @classmethod
    def from_points(cls, points):
        #https://www.johndcook.com/blog/2023/06/18/circle-through-three-points/
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]
        if ((p2.x-p1.x)*(p3.y-p1.y) != (p2.y-p1.y)*(p3.x-p1.x)) \
           and (p1!=p2) and (p1!=p3) and (p2!=p3):
            s1 = p1.x ** 2 + p1.y ** 2
            s2 = p2.x ** 2 + p2.y ** 2
            s3 = p3.x ** 2 + p3.y ** 2
            M11 = p1.x*p2.y + p2.x*p3.y + p3.x*p1.y - \
                 (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y)
            M12 = s1*p2.y + s2*p3.y + s3*p1.y - (s2*p1.y + s3*p2.y + s1*p3.y)
            M13 = s1*p2.x + s2*p3.x + s3*p1.x - (s2*p1.x + s3*p2.x + s1*p3.x)
            x = 0.5 * M12 / M11
            y = -0.5 * M13 / M11
            rad = ((p1.x-x)**2 + (p1.y-y)**2) ** 0.5
            return cls(x, y, rad)
        else:
            raise ValueError('punkty współliniowe')

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
        return self

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

    @property
    def top(self):
        return self.p.y + self.rad
    
    @property
    def left(self):
        return self.p.x - self.rad

    @property
    def bottom(self):
        return self.p.y - self.rad

    @property
    def right(self):
        return self.p.x + self.rad

    @property
    def width(self):
        return self.rad * 2

    @property
    def height(self):
        return self.rad * 2

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def topleft(self):
        return Point(self.left, self.top)
