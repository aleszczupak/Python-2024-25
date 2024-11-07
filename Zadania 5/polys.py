from itertools import zip_longest
from functools import reduce

def add_poly(poly1, poly2):
    polysum = [sum(t) for t in zip_longest(poly1, poly2, fillvalue=0)]
    polysum = cut_zeros(polysum)
    return polysum

def sub_poly(poly1, poly2):
    polysub = [t1-t2 for t1, t2 in zip_longest(poly1, poly2, fillvalue=0)]
    polysub = cut_zeros(polysub)
    return polysub

def mul_poly(poly1, poly2):
    polymul = [0] * (len(poly1) + len(poly2) - 1)
    for i, c1 in enumerate(poly1):
        for j, c2 in enumerate(poly2):
            polymul[i + j] += c1 * c2
    polymul = cut_zeros(polymul)
    return polymul        

def is_zero(poly):
    return False if any(poly) else True

def eq_poly(poly1, poly2):
    poly1 = cut_zeros(poly1)
    poly2 = cut_zeros(poly2)
    return True if poly1 == poly2 else False

def eval_poly(poly, x):
    return reduce(lambda a, b: a * x + b, reversed(poly))

def pow_poly(poly, n):
    poly = cut_zeros(poly)
    polypow = [1]
    for i in range(n):
        polypow = mul_poly(polypow, poly)
    return polypow

def diff_poly(poly):
    poly = cut_zeros(poly)
    polydiff = []
    ex = 1
    for i in range(1, len(poly)):
        polydiff.append(poly[i] * ex)
        ex += 1
    return polydiff

def combine_poly(poly1, poly2):
    polycomb = [0]
    for exp, coeff in enumerate(poly1):
        polycomb = add_poly(polycomb, mul_poly([coeff], pow_poly(poly2, exp)))
    return polycomb

def cut_zeros(poly):
    '''Funkcja obcinająca niepotrzebne zera z końca listy współczynników
    wielomianu.'''
    while poly[-1] == 0 and len(poly) > 1:
        del poly[-1]
    return poly
