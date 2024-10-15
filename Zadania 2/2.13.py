#with open('outfile.txt', 'r') as file:
#    line = file.read()

line = 'Pierwsza linijka\tto jest\na teraz druga!\ntrzecia\nGvR\tkoniec.'

words = line.split()
total_len = sum([len(word) for word in words])
print(total_len)
