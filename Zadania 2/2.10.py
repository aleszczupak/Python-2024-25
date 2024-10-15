with open('infile.txt', 'r') as file:
    line = file.read()

# domyślnie każdy biały znak jest separatorem split()
num_of_words = len(line.split())
assert num_of_words == 16
print(num_of_words)
