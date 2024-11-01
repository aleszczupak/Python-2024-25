def flatten(sequence):
    '''Funkcja zwracająca spłaszczoną listę wszystkich elementów sekwencji.'''
    flat_seq = []
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            flat_seq.extend(flatten(subs)) # rekurencja
        else:
            flat_seq.append(subs)
    return flat_seq

s = [1,(2,3),[],[4,(5,6,7)],8,[9]]
assert flatten(s) == list(range(1, 10))            
print(flatten(s))
