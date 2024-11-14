import math

class Frac:
    '''Klasa reprezentująca ułamek.'''

    def __init__(self, x=0, y=1):
        # kod upraszczający ułamek
        gcd = math.gcd(abs(x), abs(y))
        self.x = x // gcd
        self.y = y // gcd
        if self.x > 0 and self.y < 0:
            self.y = abs(self.y)
            self.x *= -1
        elif self.x < 0 and self.y < 0:
            self.x = abs(self.x)
            self.y = abs(self.y)
        elif self.y == 0:
            raise ZeroDivisionError

    def __str__(self):
        if self.y == 1 or self.x == 0:
            return str(self.x)
        else:
            return str(self.x) + '/' + str(self.y)

    def __repr__(self):
        if self.y == 1 or self.x == 0:
            return 'Frac(' + str(self.x) + ')'
        else:
            return 'Frac(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.x/self.y) < (other.x/other.y)

    def __le__(self, other):
        return (self.x/self.y) <= (other.x/other.y)

    def __gt__ (self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        newx = self.x * other.y + self.y * other.x
        newy = self.y * other.y
        return Frac(newx, newy)

    def __sub__(self, other):
        newx = self.x * other.y - self.y * other.x
        newy = self.y * other.y
        return Frac(newx, newy)

    def __mul__(self, other):
        newx = self.x * other.x
        newy = self.y * other.y
        return Frac(newx, newy)

    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError
        newx = self.x * other.y
        newy = self.y * other.x
        return Frac(newx, newy)

    def __floordiv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError
        return (self.x/self.y) // (other.x/other.y)

    def __mod__(self, other):
        if other.x == 0:
            raise ZeroDivisionError
        return (self.x/self.y) % (other.x/other.y)

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-1 * self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def float(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))
