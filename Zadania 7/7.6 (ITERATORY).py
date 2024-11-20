import itertools
import random

def iterator_a(n):
    # wypisuje n razy parę '0, 1'
    #it = itertools.repeat('0, 1')
    # wypisuje kolejno 0, 1 n razy
    #it = itertools.cycle([0, 1])
    it = itertools.chain.from_iterable(['0', '1'] * n)
    for i in range(n):
        print(next(it), end=', ')

def iterator_b(n):
    #it = iter(lambda: random.choice(['N', 'E', 'S', 'W']), 1)
    it = (random.choice(['N', 'E', 'S', 'W']) for _ in iter(str, 1))
    for i in range(n):
        print(next(it), end=', ')

def iterator_c(n):
    # n razy wypisuje WSZYSTKIE dni tygodnia
    #for j, i in enumerate(itertools.repeat('0, 1, 2, 3, 4, 5, 6')):
    for j, i in enumerate(itertools.repeat(', '.join(str(d) for d in
                                                     list(range(7))))):
    # wypisuje kolejno n dni tygodnia
    #for j, i in enumerate(itertools.chain.from_iterable(list(str(d) for d in
    #                                                         range(7)) * n)):
    #for j, i in enumerate(itertools.cycle(range(7))):
        if j >= n:
            break
        else:
            print(i, end=', ')

iterator_a(20)
print('\n\n')
iterator_b(25)
print('\n\n')
iterator_c(28)
