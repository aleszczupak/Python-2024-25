seq1 = 'toronto123'
seq2 = 'tokio345'
seq3 = 'wowondo012'

# sposób 1
a = []
b = []

for i in seq1:
    for j in seq2:
        if i == j:
            if i not in a:
                a.append(i)
for i in seq1+seq2:
    if i not in b:
        b.append(i)

print(a)
print(b)
print()

# sposób 2
set1 = set(seq1)
set2 = set(seq2)
print(set1 & set2)
print(set1 | set2)
print()

# sposób 3
def fa(seq1, seq2):
    a = []
    smin = min([seq1, seq2], key=lambda s:(len(s), s))
    smax = max([seq1, seq2], key=lambda s:(len(s), s))
    for s in smin:
        if s in smax and s not in a:
            a.append(s)
    return a
        
def fb(seq1, seq2):
    b = []
    for seq in [seq1, seq2]:
        for s in seq:
            if not s in b:
                b.append(s)
    return b

print(fa(seq1, seq2))
print(fb(seq1, seq2))
print(fa(seq1, seq3))
print(fb(seq1, seq3))
print()

# sposób 4
a = set([s for s in min([seq1, seq3], key=lambda s:(len(s), s))
         if s in max([seq1, seq3], key=lambda s:(len(s), s))])
b = set([s for s in seq1+seq3])
print(a)
print(b)
