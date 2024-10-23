# 1 - jest poprawny, średniki po 'result = ...' nie są potrzebne
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
    
# 2 - niepoprawny
# for i in 'axby': if ord(i) < 100: print(i)
# poprawna wersja
for i in 'axby':
    if ord(i) < 100: print(i)

# 3 - poprawny
for i in 'axby': print(ord(i) if ord(i) < 100 else i)
