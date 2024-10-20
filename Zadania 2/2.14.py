with open('outfile.txt', 'r') as file:
    line = file.read()
    
#line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'
   
words = line.split()

# sposób 1
words.sort(key=len, reverse=True)
print(words[0], len(words[0]))

# sposób 2 - wydajnieszy
max_word = max(words, key=len)
print(max_word, len(max_word))

assert (words[0] == 'komentarz' and len(words[0]) == 9)
assert (max_word == 'komentarz' and len(max_word) == 9)
#assert (words[0] == 'Pierwsza' and len(words[0]) == 8)
#assert (max_word == 'Pierwsza' and len(max_word) == 8)
