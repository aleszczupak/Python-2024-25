# korzystając z gotowej funkcji reverse()
def odwracanie(L, left, right):
    '''Funkcja odwracającą kolejność elementów na liście od numeru left do
    right włącznie. Wersja z reverse().'''
    try:
        if left > right:
            left, right = right, left
        subL = L[left:(right+1)]
        subL.reverse()
        L[left:(right+1)] = subL
        return L
    except TypeError:
        return('nieprawidłowy indeks')

print(odwracanie([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(odwracanie([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'ola', 2))
print(odwracanie([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))
print()

def odwracanie_iter(L, left, right):
    '''Funkcja odwracającą kolejność elementów na liście od numeru left do
    right włącznie. Wersja iteracyjna.'''
    try:
        if left == right:
            pass
        else:
            if left > right:
                left, right = right, left
            for i in range(left, right//2+2):
                L[i], L[right] = L[right], L[i]
                right -= 1
        return L
    except TypeError:
        return('nieprawidłowy indeks')    

print(odwracanie_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(odwracanie_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 2))
print(odwracanie_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))        
print()

def odwracanie_rek(L, left, right):
    '''Funkcja odwracającą kolejność elementów na liście od numeru left do
    right włącznie. Wersja rekurencyjna.'''
    try:
        if left == right:
            return L
        else:
            if left >= right:
                left, right = right, left
            L[left], L[right] = L[right], L[left]
            return odwracanie_rek(L, left+1, right-1)
    except TypeError:
        return('nieprawidłowy indeks')    

print(odwracanie_rek([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(odwracanie_rek([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 2))
print(odwracanie_rek([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))
