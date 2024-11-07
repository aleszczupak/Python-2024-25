def add_sparse_poly(poly1, poly2):
    '''
    >>> add_sparse_poly({0: 3, 1: 7, 5: -8}, {0: 1, 2: -4})
    {0: 4, 1: 7, 5: -8, 2: -4}
    >>> add_sparse_poly({5: 0}, {0: 1, 2: -4})
    {0: 1, 2: -4}
    '''
    poly1 = new_poly(poly1)
    poly2 = new_poly(poly2)
    poly3 = dict()
    for key in poly1:
        poly3[key] = poly3.get(key, 0) + poly1[key]
    for key in poly2:
        poly3[key] = poly3.get(key, 0) + poly2[key]
        if poly3[key] == 0:
            del poly3[key]
    if not poly3:
        poly3[0] = 0
    return poly3

def sub_sparse_poly(poly1, poly2):
    '''
    >>> sub_sparse_poly({0: 3, 1: 7, 5: -8}, {1: -8, 3: 3})
    {0: 3, 1: 15, 5: -8, 3: -3}
    >>> sub_sparse_poly({1: 2, 3: 5}, {1: 2, 3: 5})
    {0: 0}
    '''
    poly1 = new_poly(poly1)
    poly2 = new_poly(poly2)
    poly3 = dict(poly1)
    for key in poly2:
        poly3[key] = poly3.get(key, 0) - poly2[key]
        if poly3[key] == 0:
            del poly3[key]
    if not poly3:
        poly3[0] = 0            
    return poly3

def mul_sparse_poly(poly1, poly2):
    '''
    >>> mul_sparse_poly({0: 3, 1: 7, 5: -8}, {1: -8, 3: 3})
    {1: -24, 3: 9, 2: -56, 4: 21, 6: 64, 8: -24}
    >>> mul_sparse_poly({5: 0}, {3: -4})
    {0: 0}
    '''
    poly3 = dict()
    for key1 in poly1:
        for key2 in poly2:
            if poly1[key1] * poly2[key2] != 0:
                poly3[key1+key2] = poly3.get((key1+key2), 0) +\
                                   poly1[key1] * poly2[key2]
    if not poly3:
        poly3[0] = 0
    return poly3       

def is_sparse_zero(poly):
    '''
    >>> is_sparse_zero({2: -4, 0: 1})
    False
    >>> is_sparse_zero({})
    True
    >>> is_sparse_zero({0: 0})
    True
    >>> is_sparse_zero({5: 0})
    True
    '''
    if poly:
        for key, val in poly.items():
            return False if val != 0 else True
    else:
        return True

def eq_sparse_poly(poly1, poly2):
    '''
    >>> eq_sparse_poly({0: 1, 2: -4}, {2: -4, 0: 1})
    True
    >>> eq_sparse_poly({1: -8, 3: 3}, {2: -4, 0: 1})
    False
    >>> eq_sparse_poly({5: 0}, {4: 0})
    True
    '''
    poly1 = new_poly(poly1)
    poly2 = new_poly(poly2)
    return True if poly1 == poly2 else False

def eval_sparse_poly(poly, x):
    '''
    >>> eval_sparse_poly({0: 3, 1: 7, 5: -8}, 2)
    -239
    >>> eval_sparse_poly({0: 3, 1: 7, 5: -8}, 0)
    3
    >>> eval_sparse_poly({5: 0}, 7)
    0
    '''
    result = 0
    for key, val in poly.items():
        result += val * x ** key
    return result

def pow_sparse_poly(poly, n):
    '''
    >>> pow_sparse_poly({1: -8, 3: 3}, 3)
    {3: -512, 5: 576, 7: -216, 9: 27}
    >>> pow_sparse_poly({0: 1, 2: -4}, 4)
    {0: 1, 2: -16, 4: 96, 6: -256, 8: 256}
    >>> pow_sparse_poly({0: 3}, 3)
    {0: 27}
    >>> pow_sparse_poly({5: 0}, 2)
    {0: 0}
    '''
    polypow = poly
    if n == 0:
        polypow = {0: 1}
    else:
        for i in range(n-1):
            polypow = mul_sparse_poly(polypow, poly)
    return polypow

def diff_sparse_poly(poly):
    '''
    >>> diff_sparse_poly({0: 3, 1: 7, 5: -8, 2: 0})
    {0: 7, 4: -40}
    >>> diff_sparse_poly({0: 1, 2: -4})
    {1: -8}
    >>> diff_sparse_poly({0: 3})
    {0: 0}
    >>> diff_sparse_poly({5: 0})
    {0: 0}
    '''
    polydiff = {}
    for key in poly:
        if key > 0 and key * poly[key] != 0:
            polydiff[key-1] = key * poly[key]
    if not polydiff:
        polydiff[0] = 0
    return polydiff

def combine_sparse_poly(poly1, poly2):
    '''
    >>> combine_sparse_poly({2: 2, 1: 3}, {1: 7, 0: -1})
    {2: 98, 1: -7, 0: -1}
    >>> combine_sparse_poly({0: 2, 2: -3}, {1: 3, 2: 2})
    {0: 2, 2: -27, 3: -36, 4: -12}
    '''
    polycomb = {}
    for key, val in poly1.items():
        polycomb = add_sparse_poly(polycomb,\
                        mul_sparse_poly({0: val},\
                            pow_sparse_poly(poly2, key)))
    return polycomb

def new_poly(poly):
    '''Funkcja usuwająca niepotrzebne pary tj. z wartościami równymi zero.
    >>> new_poly({5: 0, 3: 1})
    {3: 1}
    '''
    newpoly = {x: a for x, a in poly.items() if a != 0}
    return newpoly

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=2)
