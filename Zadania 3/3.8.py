seq1 = 'toronto123'
seq2 = 'tokio345'

# sposób 1, niezbyt wydajny
a = []
b = []

for i in seq1:
    if i not in a:
        a.append(i)
    if i not in b:
        b.append(i)        

n = len(a)
i = 0
while i < n:
    if a[i] not in seq2:
        del a[i]
        n -= 1
        i -= 1
    i += 1

for j in seq2:
    if j not in b:
        b.append(j)

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
def fa(*args):
    a = []
    smin = min(args, key=len)
    smax = max(args, key=len)
    for s in smin:
        if s in smax and s not in a:
            a.append(s)
    return a
        
def fb(*args):
    b = []
    for seq in args:
        for s in seq:
            if not s in b:
                b.append(s)
    return b

print(fa(seq1, seq2))
print(fb(seq1, seq2))
print()

# sposób 4
a = set([s for s in min([seq1, seq2], key=len) if s in max([seq1, seq2],
                                                           key=len)])
b = set([s for s in seq1+seq2])
print(a)
print(b)
