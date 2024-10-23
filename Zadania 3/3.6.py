rows = int(input('Podaj ilość wierszy:\n'))
cols = int(input('Podaj ilość kolumn:\n'))

aline = '+'
bline = '|'
grid = ''

for i in range(cols):
    aline += '---+'
    bline += '   |'

for i in range(rows):
    grid += aline + '\n' + bline + '\n'

grid += aline
print(grid)
