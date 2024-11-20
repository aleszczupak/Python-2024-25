class Frac:
    '''Klasa reprezentująca ułamek.'''

    @staticmethod
    def gcd(m, n):
        if m % n == 0:
            return n
        else:
            return Frac.gcd(n, m%n)    

    def __init__(self, x=0, y=1):
        gcd = Frac.gcd(abs(x), abs(y))
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
            return '{}/{}'.format(self.x, self.y)

    def __repr__(self):
        if self.y == 1 or self.x == 0:
            return 'Frac({})'.format(self.x)
        else:
            return 'Frac({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        gcd = Frac.gcd(self.y, other.y)
        return (gcd / self.y * self.x) < (gcd / other.y * other.x)

    def __le__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        gcd = Frac.gcd(self.y, other.y)
        return (gcd / self.y * self.x) <= (gcd / other.y * other.x)

    def __gt__ (self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        newx = self.x * other.y + self.y * other.x
        newy = self.y * other.y
        return Frac(newx, newy)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        newx = self.x * other.y - self.y * other.x
        newy = self.y * other.y
        return Frac(newx, newy)

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        newx = self.x * other.x
        newy = self.y * other.y
        return Frac(newx, newy)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            other = Frac(x, y)
        if other.x == 0 or other == 0:
            raise ZeroDivisionError
        newx = self.x * other.y
        newy = self.y * other.x
        return Frac(newx, newy)

    def __rtruediv__(self, other):
        if self.x == 0:
            raise ZeroDivisionError
        return Frac(self.y * other, self.x)

    def __floordiv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError
        newx = self.x * other.y
        newy = self.y * other.x
        return Frac(newx // newy)

    def __mod__(self, other):
        if other.x == 0:
            raise ZeroDivisionError
        return self - (self // other) * other

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-1 * self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))
