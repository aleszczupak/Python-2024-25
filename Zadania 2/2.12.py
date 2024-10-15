#with open('outfile.txt', 'r') as file:
#    line = file.read()

line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'
print(line, \'n')

words = line.split()

# sposób 1 - wolniejszy
first_letters_word1 = ''
last_letters_word1 = ''

for i in range(len(words)):
    first_letters_word1 += words[i][0]

for i in range(len(words)):
    last_letters_word1 += words[i][len(words[i])-1]

print(first_letters_word1, last_letters_word1, sep='\n')

# sposób 2 - lepszy pamięciowo
first_letters = [words[i][0] for i in range(len(words))]
first_letters_word2 = ''.join(first_letters)

last_letters = [words[i][len(words[i])-1] for i in range(len(words))]
last_letters_word2 = ''.join(last_letters)

print(first_letters_word2, last_letters_word2, sep='\n')

assert first_letters_word1 == first_letters_word2
assert last_letters_word1 == last_letters_word2
