#with open('infile.txt', 'r') as file:
#    line = file.read()

line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'

new_line = line.replace('GvR', 'Guido van Rossum')
print(new_line)
