with open('outfile.txt', 'r') as file:
    line = file.read()
    
#line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'
    
words = line.split()
words.sort(key=len, reverse=True)
print(words[0], len(words[0]))

assert (words[0] == 'komentarz' and len(words[0]) == 9)
#assert (words[0] == 'Pierwsza' and len(words[0]) == 8)
