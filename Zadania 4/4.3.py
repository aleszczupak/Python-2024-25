def factorial_iter(n):
    '''Iteracyjna wersja funkcji factorial(n) obliczającej silnię.'''
    if not (isinstance(n, int) and n >= 0):
        raise TypeError('nieprawidłowa wartość')
    else:
        fact = 1
        for i in range(n):
            fact *= (i+1)
        return fact

assert factorial_iter(5) == 120
print(factorial_iter(5))
assert factorial_iter(6) == 720
print(factorial_iter(6))

# sposób z reduce oraz lambda
# jak dołączyć jeszcze warunek n>=0 za pomocą adnotacji?
def factorial_reduce(n: int) -> int:
    from functools import reduce
    return reduce(lambda a, b: a*b, list(range(1, n+1)))

assert factorial_reduce(5) == factorial_iter(5)
print(factorial_reduce(5))
assert factorial_reduce(6) == factorial_iter(6)
print(factorial_reduce(6))
