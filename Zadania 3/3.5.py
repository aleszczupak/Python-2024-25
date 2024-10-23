n = int(input('Podaj długość miarki w [cm]:\n'))

top = '|'
bottom = '0'
ruler = ''

for i in range(n):
    top +=  '....|'
    bottom += (' ' * (5 - len(str(i+1)))) + str(i+1) 

ruler = top + '\n' + bottom
print(ruler)
