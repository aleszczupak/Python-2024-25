def sum_seq(sequence):
    '''Funkcja obliczająca sume liczb zawartych w sekwencji, która może
    zawierać zagnieżdżone podsekwencje.'''
    s = 0
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            s += sum_seq(subs) # rekurencja
        elif isinstance(subs, (float, int)):
            s += subs
        else:
            raise TypeError('nieprawidłowy typ danych')
    return s

print(sum_seq([1, (2, 3, 1), [5, 2, 2], [], [0, 2, 3], 5, 3, (1, 1), [3]]))
print(sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]))
print(sum_seq([1,(2,3),[],['ola',(5,6,7)],8,[9]]))
