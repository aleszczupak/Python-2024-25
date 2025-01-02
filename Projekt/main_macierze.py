'''
Aleksandra Szczupak

Projekt zaliczeniowy kursu Język Python 2024/25

*** MACIERZE ***

Macierze gęste na bazie list Pythona. Elementy macierzy są zapisywane wierszami
na liście.
'''

from macierze import *

print('\n>>>counter:', Matrix.counter, '#0')
print()

# instancje klasy
m1 = Matrix(4, 3)
m1[0, 0] = 1
m1[0, 1] = 1.5
m1[0, 2] = 4
m1[1, 0] = -1
m1[1, 1] = 2
m1[2, 0] = 2.75
m1[2, 1] = 4
m1[2, 2] = -5
m1[3, 0] = 1.125
m1[3, 1] = 9
m1[3, 2] = 3

m2 = Matrix.from_matrix([[1, 1.5, 4], [-1, 2, 0], [2.755, 4, -5], [1.12, 9, 3]])

m3 = Matrix.from_matrix([[1, 2, 3, 8], [4, 0, 5, 0], [-7, 9, -2, -6]])

m4 = Matrix(5, 5)
m4[0, 3] = 3
m4[0, 4] = 4
m4[1, 0] = -1
m4[1, 4] = 7
m4[2, 1] = 6
m4[2, 2] = 15
m4[3, 3] = 1.5
m4[3, 4] = 4
m4[4, 0] = 1.5
m4[4, 2] = -2
m4[4, 3] = 1

m5 = Matrix(2, 2)
m5[0, 0] = 1
m5[0, 1] = 2
m5[1, 0] = 3
m5[1, 1] = 4

m6 = Matrix(1, 1)
m6[0, 0] = 5

m7 = Matrix.from_matrix([[1, 2.0004], [3, 4.0004]])

m8 = Matrix(2, 2)
m8[0, 1] = 1
m8[1, 1] = -1

m9 = Matrix(2, 2)
m9[0, 0] = 1
m9[0, 1] = 2
m9[1, 0] = 3
m9[1, 1] = 4

instances = [m1, m2, m3, m4, m5, m6, m7, m8, m9]

print('>>>counter:', Matrix.counter, '#9')
print()

# sprawdzenie
print('*** MACIERZE ***')
print()

# __repr__
print('*** METODA __repr__ ***')
for num, ins in enumerate(instances):
    print('macierz', num+1)
    print(repr(ins))
    print()
print()

# __str__
print('*** METODA __str__ ***')
for num, ins in enumerate(instances):
    print('macierz', num+1)
    print(ins)
    print()
print('>>>counter:', Matrix.counter, '#9')
print()

# __getitem___
print('*** METODA __getitem__ ***')
print('m3[1, 2] #5')
print(m3[1, 2])
print()
print('m4[4, 4] #0')
print(m4[4, 4])
print('>>>counter:', Matrix.counter, '#9')
print()
print()

# __setitem__
print('*** METODA __setitem__ ***')
print('m8[0, 0] = 7')
m8[0, 0] = 7
print(m8)
print('>>>counter:', Matrix.counter, '#9')
print()
print('m8[0, 0] = 0')
m8[0, 0] = 0
print(m8)
print()
print()

# __eq__
print('*** METODA __eq__ ***')
print('m1 == m1 #True')
print(m1 == m1)
print('>>>counter:', Matrix.counter, '#9')
print()
print('m1 == m2 #False')
print(m1 == m2)
print()
print('m5 == m6 #False')
print(m5 == m6)
print()
print('m5 == m9 #True')
print(m5 == m9)
print()
print()

# __ne__
print('*** METODA __ne__ ***')
print('m1 != m1 #False')
print(m1 != m1)
print()
print('m1 != m2 #True')
print(m1 != m2)
print()
print('m5 != m6 #True')
print(m5 != m6)
print()
print('m5 != m9 #False')
print(m5 != m9)
print()
print()

# equal_round
print('*** METODA equal_round ***')
print('m1.equal_round(m2) #False')
print(m1.equal_round(m2))
print()
print('m5.equal_round(m7) #True')
print(m5.equal_round(m7))
print()
print('m7.equal_round(m5) #True')
print(m7.equal_round(m5))
print()
print('m4.equal_round(m8) #False')
print(m4.equal_round(m8))
print()
print()

# __add__
print('*** METODA __add__ ***')
print('m1 + m2')
print(m1 + m2)
print(repr(m1 + m2))
print('>>>counter:', Matrix.counter, '#9')
print()
print('m8 + m8 + m8')
print(m8 + m8 + m8)
print(repr(m8 + m8 + m8))
print('>>>counter:', Matrix.counter, '#9')
print()
print()

# __iadd__
print('*** METODA __iadd__ ***')
print('m5')
print(m5)
print()
print('id(m5)')
print(id(m5))
print()
print('m5copy1 = copy(m5)')
m5copy1 = copy(m5)
print()
print('id(m5copy1)')
print(id(m5copy1))
print('>>>counter:', Matrix.counter, '#10')
print()
print('m5copy1 += m5')
m5copy1 += m5
print('>>>counter:', Matrix.counter, '#10')
print()
print('m5copy1')
print(m5copy1)
print(repr(m5copy1))
print()
print('id(m5copy1)')
print(id(m5copy1))
print('>>>counter:', Matrix.counter, '#10')
print()
print('m5')
print(m5)
print()
print('id(m5)')
print(id(m5))
print('>>>counter:', Matrix.counter, '#10')
print()
print('m8copy1 = copy(m8)')
m8copy1 = copy(m8)
print('>>>counter:', Matrix.counter, '#11')
print()
print('m8copy1 += m7')
m8copy1 += m7
print('>>>counter:', Matrix.counter, '#11')
print()
print('m8copy1')
print(m8copy1)
print(repr(m8copy1))
print('>>>counter:', Matrix.counter, '#11')
print()
print('m8')
print(m8)
print('>>>counter:', Matrix.counter, '#11')
print()
print('m9')
print(m9)
print()
print()

# __sub__
print('*** METODA __sub__ ***')
print('m1 - m2')
print(m1 - m2)
print(repr(m1 - m2))
print('>>>counter:', Matrix.counter, '#11')
print()
print('m5s8 = m5 - m8')
m5s8 = m5 - m8
print()
print('m5s8')
print(m5s8)
print(repr(m5s8))
print('>>>counter:', Matrix.counter, '#12')
print()
print()

# __isub__
print('*** METODA __isub__ ***')
print('m5')
print(m5)
print()
print('id(m5)')
print(id(m5))
print()
print('m5copy2 = copy(m5)')
m5copy2 = copy(m5)
print()
print('id(m5copy2)')
print(id(m5copy2))
print('counter:', Matrix.counter, '#13')
print()
print('m5copy2 -= m5')
m5copy2 -= m5
print('>>>counter:', Matrix.counter, '#13')
print()
print('m5copy2')
print(m5copy2)
print()
print('id(m5copy2)')
print(id(m5copy2))
print('>>>counter:', Matrix.counter, '#13')
print()
print('m5')
print(m5)
print()
print('id(m5)')
print(id(m5))
print('>>>counter:', Matrix.counter, '#13')
print()
print('m9 -= m5')
print()
print()

# __mul__
print('*** METODA __mul__ ***')
print('m1 * m3')
print(m1 * m3)
print('>>>counter:', Matrix.counter, '#13')
print()
print('m3 * m1')
print(m3 * m1)
print()
print('m5 * m8')
print(m5 * m8)
print(repr(m5 * m8))
print('>>>counter:', Matrix.counter, '#13')
print()
print('m2 * 10')
print(m2 * 10)
print('>>>counter:', Matrix.counter, '#13')
print()
print('10 * m2')
print(10 * m2)
print('>>>counter:', Matrix.counter, '#13')
print()
print()

# __imul__
print('*** METODA __imul__ ***')
print('m5copy3 = copy(m5)')
m5copy3 = copy(m5)
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5copy3 *= m5')
m5copy3 *= m5
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5copy3')
print(m5copy3)
print(repr(m5copy3))
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5')
print(m5)
print('>>>counter:', Matrix.counter, '#14')
print()
print()

# __pow__
print('*** METODA __pow__ ***')
print('m5 ** 0')
print(m5 ** 0)
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5 ** 1')
print(m5 ** 1)
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5 ** 2')
print(m5 ** 2)
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5 ** 3')
print(m5 ** 3)
print('>>>counter:', Matrix.counter, '#14')
print()
print('m5p4 = m5 ** 4')
m5p4 = m5 ** 4
print()
print('m5p4')
print(m5p4)
print('>>>counter:', Matrix.counter, '#15')
print()
print()

# __truediv__
print('*** METODA __truediv__ ***')
print('m5 / 5')
print(m5 / 5)
print('>>>counter:', Matrix.counter, '#15')
print()
print('m5 / 0.5')
print(m5 / 0.5)
print('>>>counter:', Matrix.counter, '#15')
print()
print()

# __itruediv__
print('*** METODA __itruediv__ ***')
print('m5copy4 = copy(m5)')
m5copy4 = copy(m5)
print('>>>counter:', Matrix.counter, '#16')
print()
print('m5copy4 /= 5')
m5copy4 /= 5
print('>>>counter:', Matrix.counter, '#16')
print()
print('m5copy4')
print(m5copy4)
print('>>>counter:', Matrix.counter, '#16')
print()
print('m5')
print(m5)
print('>>>counter:', Matrix.counter, '#16')
print()
print()

# @property transpose
print('*** METODA @property transpose ***')
print('m3')
print(m3)
print()
print('id(m3)')
print(id(m3))
print()
print('m3t = m3.transpose')
m3t = m3.transpose
print(m3t)
print()
print('id(m3t)')
print(id(m3t))
print('>>>counter:', Matrix.counter, '#17')
print()
print('m3t[1, 0]')
print(m3t[1, 0])
print()
print('m3t[1, 0] = 222')
m3t[1, 0] = 222
print('m3t')
print(m3t)
print()
print('m3')
print(m3)
print('>>>counter:', Matrix.counter, '#17')
print()
print()

# reshape
print('*** METODA reshape ***')
print('m3.reshape(4, 3)')
print(m3.reshape(4, 3))
print('>>>counter:', Matrix.counter, '#17')
print()
print('m3.reshape(2, 6)')
print(m3.reshape(2, 6))
print('>>>counter:', Matrix.counter, '#17')
print()
print('m84x1 = m8.reshape(4, 1)')
m84x1 = m8.reshape(4, 1)
print()
print('m84x1')
print(m84x1)
print('>>>counter:', Matrix.counter, '#18')
print()
print()

# @property trace
print('*** METODA @property trace ***')
print('m4.trace')
print(m4.trace)
print('>>>counter:', Matrix.counter, '#18')
print()
print('m7.trace')
print(m7.trace)
print()
print()

# @property determinant
print('*** METODA @property determinant ***')
print('m4.determinant')
print(m4.determinant)
print('>>>counter:', Matrix.counter, '#18')
print()
print('m5.determinant')
print(m5.determinant)
print('>>>counter:', Matrix.counter, '#18')
print()
print('m6.determinant')
print(m6.determinant)
print()
print('m8.determinant')
print(m8.determinant)
print()
print()

# submatrix
print('*** METODA submatrix ***')
print('m4.submatrix(0, 0)')
print(m4.submatrix(0, 0))
print('>>>counter:', Matrix.counter, '#18')
print()
print('m1sub21 = m1.submatrix(2, 1)')
m1sub21 = m1.submatrix(2, 1)
print('m1sub21')
print(m1sub21)
print('>>>counter:', Matrix.counter, '#19')
print()
print()

# @property inverse
print('*** METODA @property inverse ***')
print('m5.inverse')
print(m5.inverse)
print(repr(m5.inverse))
print('>>>counter:', Matrix.counter, '#19')
print()
print('m6.inverse')
print(m6.inverse)
print('>>>counter:', Matrix.counter, '#19')
print()
print('m4inv = m4.inverse')
m4inv = m4.inverse
print('m4inv')
print(m4inv)
print('>>>counter:', Matrix.counter, '#20')
print()
print()

# @classmethod identity
print('*** METODA @classmethod identity ***')
print('Matrix.identity(5)')
print(Matrix.identity(5))
print('>>>counter się nie zmienia')
print('>>>counter:', Matrix.counter, '#20')
print()
print('identity1 = Matrix.identiy(1)')
identity1 = Matrix.identity(1)
print()
print('identity1')
print(identity1)
print('>>>counter:', Matrix.counter, '#21')
print()
print()

# @classmethod from_matrix
print('*** METODA @classmethod from_matrix ***')
print('Matrix.from_matrix([[1, 2], [3, 4]])')
print(Matrix.from_matrix([[1, 2], [3, 4]]))
print('>>>counter się nie zmienia')
print('>>>counter:', Matrix.counter, '#21')
print()
print('mfm = Matrix.from_matrix([[0, 1], [0, -1]])')
mfm = Matrix.from_matrix([[0, 1], [0, -1]])
print()
print('mfm')
print(mfm)
print('>>>counter:', Matrix.counter, '#22')
print()
print()

# __del__
print('*** METODA __del__ ***')
print('m6')
print(m6)
print()
print('id(m6)')
print(id(m6))
print('>>>counter:', Matrix.counter, '#22')
print()
print('del m6')
del m6
print('>>>counter się nie zmienia')
print('>>>counter:', Matrix.counter, '#22')
print()
print('m6 = Matrix(1, 1)\nm6[0, 0] = 5\nm6')
m6 = Matrix(1, 1)
m6[0, 0] = 5
print(m6)
print()
print('id(m6)')
print(id(m6))
print('>>>counter:', Matrix.counter, '#23')
print()
print()

# wiele metod
print('*** WIELE METOD ***')
print('((m1 + m2) * m3 / 2).transpose')
print()
print(((m1 + m2) * m3 / 2).transpose)
print('>>>counter:', Matrix.counter, '#23')
print()
print('multi = m8 - m8 * m5 * 2')
multi = m8 - m8 * m5 * 2
print()
print('multi')
print(multi)
print('>>>counter:', Matrix.counter, '#24')
print()
print()
