def fibonacci_iter(n):
    '''Iteracyjna wersja funkcji fibonacci(n) obliczającej n-ty wyraz
    ciągu Fibonacciego.'''
    if not (isinstance(n, int) and n >= 0):
        raise TypeError('nieprawidłowa wartość')
    else:
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a + b
        return b

assert fibonacci_iter(1) == 1
print(fibonacci_iter(1))
assert fibonacci_iter(5) == 5
print(fibonacci_iter(5))
assert fibonacci_iter(10) == 55
print(fibonacci_iter(10))
