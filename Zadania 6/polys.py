from itertools import zip_longest
from functools import reduce

class Poly:
    '''Klasa reprezentująca wielomiany.'''

    def __init__(self, *coeffs):
        coeffs = list(coeffs)
        while coeffs[-1] == 0 and len(coeffs) > 1:
            coeffs.pop()
        self.poly = coeffs

    def __str__(self):
        return str(self.poly)     

    def __add__(self, other):
        poly1 = self.poly
        poly2 = other.poly
        polysum = [sum(t) for t in zip_longest(poly1, poly2, fillvalue=0)]
        return Poly(*polysum)

    def __sub__(self, other):
        poly1 = self.poly
        poly2 = other.poly
        polysub = [t1-t2 for t1, t2 in zip_longest(poly1, poly2, fillvalue=0)]
        return Poly(*polysub)

    def __mul__(self, other):
        poly1 = self.poly
        poly2 = other.poly
        polymul = [0] * (len(poly1) + len(poly2) - 1)
        for i, c1 in enumerate(poly1):
            for j, c2 in enumerate(poly2):
                polymul[i + j] += c1 * c2
        return Poly(*polymul)

    def __pos__(self):
        return self

    def __neg__(self):
        poly = self.poly
        polyneg = [-coeff for coeff in poly]
        return Poly(*polyneg)

    def __eq__(self, other):
        poly1 = self.poly
        poly2 = other.poly
        #return poly1 == poly2
        return all(c1 == c2 for (c1, c2) in zip_longest(poly1, poly2,
                                                        fillvalue=0))

    def __ne__(self, other):
        return not self == other

    def eval(self, x):
        poly = self.poly
        result = 0
        for c in reversed(poly):
            result = result * x + c
        return result
        #return reduce(lambda a, b: a * x + b, reversed(poly))

    def __pow__(self, n):
        polypow = Poly(1)
        for i in range(n):
            polypow *= self
        return polypow

    def combine(self, other):
        polycomb = Poly(0)
        #for exp, coeff in enumerate(self.poly):
            #polycomb += (Poly(coeff) * (other ** exp))
        for c in reversed(self.poly):
            polycomb = polycomb * other + Poly(c)
        return polycomb

    def diff(self):
        poly = self.poly
        polydiff = [poly[i] * i for i in range(1, len(poly))]
        return Poly(*polydiff)      

    def integrate(self):
        poly = self.poly
        polyint = [poly[i] / (i+1) for i in range(len(poly))]
        polyint = [0] + polyint
        return Poly(*polyint)

    def is_zero(self):
        poly = self.poly
        return all(c == 0 for c in poly)
