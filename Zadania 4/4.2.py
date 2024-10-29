def make_ruler(n):
    '''Funkcja zwracająca miarkę o zadanej długości.'''
    top, bottom = '', ''
    for i in range(n):
        top += '....|'
        bottom += (' ' * (5 - len(str(i+1)))) + str(i+1) 
    ruler = '|' + top + '\n' + '0' + bottom
    return ruler

def make_grid(rows, cols):
    '''Funkcja zwracająca prostokąt zbudowany z małych kratek.'''
    aline = cols * '+---' + '+\n'
    bline = cols * '|   ' + '|\n'
    grid = rows * (aline + bline) + aline
    return grid

# z przykładów rozwiązań podanych na ćwiczeniach
def make_ruler2(n):
    '''Funkcja zwracająca miarkę o zadanej długości.'''
    ruler = []
    ruler.extend('|....' for i in range(n))
    ruler.append('|\n0')
    ruler.extend(str(i+1).rjust(5) for i in range(n))
    ruler.append('\n')
    return ''.join(ruler)

def make_grid2(rows, cols):
    '''Funkcja zwracająca prostokąt zbudowany z małych kratek.'''
    aline = '---'.join('+' * (cols+1)) + '\n'
    bline = '   '.join('|' * (cols+1)) + '\n'
    return bline.join([aline] * (rows+1))

print(make_ruler(12))
print(make_ruler2(12))
print(make_grid(2, 4))
print(make_grid2(2, 4))
