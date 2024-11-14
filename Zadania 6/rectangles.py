from points import Point

class Rectangle:
    '''Klasa reprezentująca prostokąt na płaszczyźnie.'''

    def __init__(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            raise ValueError('niepoprawne współrzędne')
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __str__(self):
        return '[' + str(self.p1) + ', ' + str(self.p2) + ']'

    def __repr__(self):
        return 'Rectangle(' + str(self.p1.x) + ', ' + str(self.p1.y) + ', ' +\
               str(self.p2.x) + ', ' + str(self.p2.y) + ')'

    def __eq__(self, other):
        return (self.p1 == other.p1) and (self.p2 == other.p2)

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.p1.x+self.p2.x) / 2, (self.p1.y+self.p2.y) / 2) 

    def area(self):
        return abs((self.p2.x-self.p1.x) * (self.p2.y-self.p1.y))

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
