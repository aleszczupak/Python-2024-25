with open('outfile.txt', 'r') as file:
    line = file.read()

#line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'

words = line.split()

# inna kolejność wyrazów w sortowaniu przez sorted i sort dla key=len

# tworzy nową listę
words_alph = sorted(words, key=str.lower)
print(words_alph)
words_len = sorted(words, key=len)
print(words_len)
# dla takiego klucza sorted i sort dla key=len tak samo
# dwa krtyeria sortowania, jeśli długość taka sama, to jeszcze alfabetycznie
words_len_alph = sorted(words, key=lambda word:(len(word), word))
print(words_len_alph)

# zmienia oryginalną listę
words.sort(key=str.lower)
print(words)
words.sort(key=len)
print(words)

words.sort(key=str.lower)
assert words == words_alph
words.sort(key=len)
assert words == words_len_alph
