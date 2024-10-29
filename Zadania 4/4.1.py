# 1
X = 'qwerty'

def func():
    print(X)

print('1')
func()
# wynik: qwerty, ponieważ X jest zmienną globalną

# 2
X = 'qwerty'

def func():
    X = 'abc'

print('\n2')
func()
print(X)
# wynik: qwerty, ponieważ X = 'abc' jest lokalna żyje tylko wewnątrz funkcji

# 3
X = 'qwerty'

def func():
    global X
    X = 'abc'

print('\n3')
func()
print(X)
# wynik: abc, ponieważ X ustawiono na zmienną globalną, w funkcji zmieniono jej
# wartość tak, że zatrzymuje ją po wyjściu z funkcji
