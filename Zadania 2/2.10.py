with open('infile.txt', 'r') as file:
    line = file.read()

#line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'

# domyślnie każdy biały znak jest separatorem split()
num_of_words = len(line.split())
assert num_of_words == 16
#assert num_of_words == 10
print(num_of_words)
