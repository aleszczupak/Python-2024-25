'''
Aleksandra Szczupak

Projekt zaliczeniowy kursu Język Python 2024/25

*** MACIERZE ***

Macierze gęste na bazie list Pythona. Elementy macierzy są zapisywane wierszami
na liście.
'''

from copy import copy, deepcopy

class Matrix:
    '''Klasa reprezentująca macierze gęste na bazie list Pythona. Elementy
    macierzy są zapisywane wierszami na liście.'''

    counter = 0
    
    def __init__(self, rows=1, cols=1):
        '''Konstruktor.'''
        self.rows = rows
        self.cols = cols
        self.data = [0] * rows * cols
        Matrix.counter += 1

    def __repr__(self):
        '''Drukowanie zagnieżdżonej listy (lista z listami reprezentującymi
        wiersze macierzy) przedstawiającej macierz.'''
        res = [str(self.data[i*self.cols:(i+1)*self.cols])
               for i in range(self.rows)]
        res = ', '.join(res)
        res = 'Matrix([' + res + '])'
        return res

    """def __str__(self):
        '''Drukowanie macierzy w formie list wiersz po wierszu.'''
        res = ''
        for i in range(self.rows):
            res += (str(self.data[i*self.cols:(i+1)*self.cols])+'\n')
        return res"""

    def __str__(self):
        '''Drukowanie macierzy w formie list wiersz po wierszu, każda kolumna
        ma szerokość najdłuższego elementu w danej kolumnie. Wartości komórek
        wyrównane do prawej strony. Dokładność wyświetlania liczb do 3 miejsc
        po przecinku.'''
        decimals = 3
        # szerokości poszczególnych kolumn
        cols_digits = []
        res = '['
        for i in range(self.cols):
            col = []
            for j in range(self.rows):
                col.append(self.data[j*self.cols+i])
            lengths = [len(str(round(num, decimals))) for num in col]
            cols_digits.append(max(lengths))
        for i in range(self.rows):
            row = self.data[i*self.cols:(i+1)*self.cols]
            if i == 0:
                res += '['
            else:
                res += ' ['
            for j in range(self.cols):
                if len(str(round(row[j], decimals))) < cols_digits[j]:
                    if j > 0:
                        res += ' ' * (cols_digits[j]-len(str(round(row[j],
                                decimals)))+1) + str(round(row[j], decimals))
                    else:
                        res += ' ' * (cols_digits[j]-len(str(round(row[j],
                                decimals)))) + str(round(row[j], decimals))
                else:
                    if j > 0:
                        res += ' ' + str(round(row[j], decimals))
                    else:
                        res += str(round(row[j], decimals))
            if i < self.rows - 1:
                res += ']\n'
            else:
                res += ']]'
        return res

    def __getitem__(self, pair):
        '''Odczyt elementu macierzowego m[i, j].''' 
        i, j = pair
        if i < self.rows and j < self.cols:
            return self.data[i*self.cols+j]
        else:
            raise ValueError('niepoprawny indeks')

    def __setitem__(self, pair, value):
        '''Przypisanie wartości danemu elementowi macierzowemu
        m[i, j] = value.'''
        i, j = pair
        if i < self.rows and j < self.cols:
            self.data[i*self.cols+j] = value
        else:
            raise ValueError('niepoprawny indeks')

    def __eq__(self, other):
        '''Porównywanie dwóch macierzy. Dwie macierze są takie same, jeśli mają
        te same wymiary i wszystkie ich elementy macierzowe na poszczególnych
        pozycjach mają identyczne wartości (z pełną dokładnością).'''
        from itertools import zip_longest
        if self.rows == other.rows and self.cols == other.cols:
            return all(n == m for (n, m) in zip_longest(self.data, other.data,
                                                        fillvalue=0))
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def equal_round(self, other, decimals=3):
        '''Porównywanie dwóch macierzy z dokładnością domyślnie do 3 miejsc po
        przecinku. Dwie macierz są sobie w przybliżeniu równe, jeśli mają takie
        same wymiary i wszystkie ich elementy macierzowe na poszczególnych
        pozycjach mają takie same wartości do 3 miejsc po przecinku.'''
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows * self.cols):
                # problem
                # https://docs.python.org/2/library/functions.html#round
                if round(self.data[i], decimals) != \
                   round(other.data[i], decimals):
                    return False
            return True
        else:
            return False

    def __add__(self, other):
        '''Dodawanie dwóch macierzy. Operacja jest możliwa, jeśli wymiary
        obydwu macierzy są jednakowe.'''
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = [self.data[i] + other.data[i]
                               for i in range(self.rows*self.cols)]
            return new_matrix
        else:
            raise ValueError('różne wymiary macierzy')       

    __iadd__ = __add__

    def __sub__(self, other):
        '''Odejmowanie dwóch macierzy. Operacja jest możliwa, jeśli wymiary
        obydwu macierzy są jednakowe.'''
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = [self.data[i] - other.data[i]
                               for i in range(self.rows*self.cols)]
            return new_matrix
        else:
            raise ValueError('różne wymiary macierzy')

    __isub__ = __sub__

    def __mul__(self, other):
        '''Mnożenie dwóch macierzy. Operacja jest możliwa, jeśli pierwsza
        macierz A ma tyle samo kolumn - wymiar n x m, co druga macierz B wierszy
        - wymiar m x p, zaś wynikowa macierz C jest wymiaru n x p:
        c_ij = a_i1 * b_1j + a_i2 * b_2j + ... + a_in * b_nj =
             = sum_{k=1}^n a_ik * b_kj.'''
        if isinstance(other, (int, float)):
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = [self.data[i] * other
                               for i in range(self.rows*self.cols)]
            return new_matrix
        else:
            if self.cols == other.rows:
                new_matrix = Matrix(self.rows, other.cols)
                for i in range(self.rows):
                    for j in range(other.cols):
                        for k in range(other.rows):
                            new_matrix.data[i*other.cols+j] += \
                            self.data[i*self.cols+k] * other.data[k*other.cols+j]                    
                return new_matrix
            else:
                raise ValueError('niepoprawnie wymiary macierzy')

    __rmul__ = __mul__

    __lmul__ = __mul__

    __imul__ = __mul__   

    def __pow__(self, power):
        '''Potęgowanie macierzy kwadratowej. Mnożenie macierzy z samą sobą
        power-1 razy.'''
        if self.rows == self.cols:
            if power == 0:
                return self.identity(self.rows)
            else:
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = self.data[:]                
                for i in range(power-1):
                    new_matrix *= self
                return new_matrix
        else:
            raise ValueError('macierz niekwadratowa')

    def __truediv__(self, other):
        '''Dzielenie wszystkich elementów macierzy przez daną liczbę.'''
        if isinstance(other, (int, float)):
            if other != 0:
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = [self.data[i] / other
                                   for i in range(self.rows*self.cols)]
                return new_matrix
            else:
                raise ZeroDivisionError('dzielenie przez zero')
        else:
            raise ValueError('niepoprawny typ')

    __rtruediv__ = __truediv__

    __itruediv__ = __truediv__

    # atrybut wirtualny
    @property  
    def transpose(self):
        '''Transpozycja macierzy. Zamiana wierszy z kolumnami.'''
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.data[j*self.rows+i] = self.data[i*self.cols+j]
        return new_matrix

    def reshape(self, new_rows, new_cols):
        '''Zmiana wymiaru macierzy. Operacja możliwa, jeśli iloczyn nowych
        wymiarów macierzy równy jest ilocznynowi wymiarów macierzy pierwotnej
        (obydwie macierze muszą mieć jednakową ilość elementów).'''        
        if new_rows * new_cols == self.cols * self.rows:
            new_matrix = Matrix(new_rows, new_cols)
            new_matrix.data = self.data[:]
            return new_matrix
        else:
            raise ValueError('niepoprawne wymiary')

    # atrybut wirtualny
    @property
    def trace(self):
        '''Ślad macierzy kwadratowej. Suma elementów na głównej przekątnej.'''
        if self.rows == self.cols:
            tr = 0
            for i in range(self.cols):
                tr += self.data[i*self.cols+i]
            #tr = reduce(sum, [self.data[i*self.cols+i] for i in range(self.cols)])
            return tr            
        else:
            raise ValueError('macierz niekwadratowa')

    # atrybut wirtualny
    @property    
    def determinant(self):
        '''Wyznacznik macierzy kwadratowej. Rekurencyjna metoda wykorzystująca
        rozwinięcie Laplace'a względem pierwszego (i=1) wiersza:
        det(A) = \sum_{k=1}^n a_ik * D_ik, gdzie: n to wymiar macierzy,
        wiersze spełniają 1 <= i <=n, D_ij = (-1)^(i+j) det(A_ij) to
        dopełnienie algebraiczne elementu a_ij macierzy A.'''
        if self.rows == self.cols:
            if self.rows == 1:
                det = self.data[0]
            elif self.rows == 2:
                det = self.data[0]*self.data[3] - self.data[1]*self.data[2]
            else:
                # rozwinięcie Laplace'a
                det = 0
                for i in range(self.cols):
                    # minor
                    new_matrix = Matrix(self.rows-1, self.cols-1)
                    # względem pierwszego wiersza
                    temp_data = self.data[self.cols:]
                    k = i
                    for j in range(self.rows-1):
                        temp_data.pop(j*self.cols+k)
                        k -= 1
                    new_matrix.data = temp_data
                    # rekurencja
                    det += ((-1)**i) * self.data[i] * new_matrix.determinant
            return det
        else:
            raise ValueError('macierz niekwadratowa')

    def submatrix(self, i, j):
        '''Podmacierz macierzy o wymiarach n x m powstała po skreśleniu i-tego
        wiersza oraz j-tej kolumny. Wynikowa macierz ma wymiar n-1 x m-1.
        Numeracja kolumn oraz wierszy od 0 do odpowiednio n-1, m-1.'''
        if i < self.rows and j < self.cols:
            new_matrix = Matrix(self.rows-1, self.cols-1)
            # usunięcie i-tego wiersza
            temp_data = self.data[0:i*self.cols] + \
                        self.data[i*self.cols+self.cols:]
            new_data = [0] * (self.rows-1) * (self.cols-1)
            # usunięcie j-tej kolumny
            for k in range(self.rows-1):
                new_data[k*new_matrix.cols:k*new_matrix.cols+new_matrix.cols] = \
                        temp_data[k*self.cols:k*self.cols+j]+\
                        temp_data[k*self.cols+j+1:k*self.cols+self.cols]
            new_matrix.data = new_data
            return new_matrix
        else:
            raise ValueError('niepoprawne indeksy')

    # atrybut wirtualny
    @property
    def inverse(self):
        '''Macierz odwrotna macierzy kwadratowej. A^(-1) istnieje jeśli macierz
        A jest nieosobliwa, ma wyznacznik różny od zera. Metoda wykorzystująca
        macierz dopełnień algebraicznych D: A^(-1) = (D)^T / det(A).'''
        if self.rows == self.cols and self.determinant != 0:
            inv_matrix = Matrix(self.rows, self.cols)
            if self.rows == 1:
                inv_matrix.data[0] = 1 / self.data[0]
            else:
                # macierz dopełnień algebraicznych
                cof_matrix = []
                for i in range(self.rows):
                    for j in range(self.cols):
                        # podmacierz
                        new_matrix = self.submatrix(i, j)
                        # minor
                        new_det = new_matrix.determinant
                        # dopełnienie algebraiczne
                        cof_matrix.append(new_det*(-1)**(i+j))
                inv_matrix.data = cof_matrix
                # macierz dołączona
                inv_matrix = inv_matrix.transpose
                # macierz odwrotna
                inv_matrix /= self.determinant
            return inv_matrix
        else:
            raise ValueError('macierz nieodwracalna')

    # metoda związana z klasą Matrix, nie z konkretnymi jej instancjami
    @classmethod
    def identity(cls, dim):
        '''Macierz jednostkowa (kwadratowa) o wymiarze dim x dim.'''
        if isinstance(dim, int) and dim > 0:
            id_matrix = cls(dim, dim)
            for i in range(dim):
                id_matrix.data[i*dim+i] = 1
            return id_matrix
        else:
            raise ValueError('niepoprawny wymiar')

    # metoda związana z klasą Matrix, nie z konkretnymi jej instancjami
    @classmethod
    def from_matrix(cls, mtrx):
        '''Tworzenie macierzy bezpośrednio poprzez podanie zagnieżdżonej listy
        (lista z listami reprezentującymi wiersze macierzy).'''
        rows = len(mtrx)
        cols = len(mtrx[0])
        if len(set([len(row) for row in mtrx])) == 1:
            new_matrix = cls(rows, cols)
            # flatten
            new_matrix.data = sum(mtrx, [])
            return new_matrix
        else:
            raise ValueError('niepoprawne wymiary')

    def __copy__(self):
        '''Kopia płytka.'''
        matrix_copy = Matrix(self.rows, self.cols)
        matrix_copy.data = self.data
        return matrix_copy

    def __deepcopy__(self, memo):
        '''Kopia głęboka.'''
        matrix_deepcopy = Matrix(self.rows, self.cols)
        matrix_deepcopy.data = self.data
        return matrix_deepcopy

    def __del__(self):
        '''Destruktor.'''
        Matrix.counter -= 1
