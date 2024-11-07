def add_sparse_matrix(sparse1, sparse2):
    sparse3 = dict()
    for pair in sparse1:
        sparse3[pair] = sparse3.get(pair, 0) + sparse1[pair]
    for pair in sparse2:
        sparse3[pair] = sparse3.get(pair, 0) + sparse2[pair]
    return new_sparse_matrix(sparse3)

def sub_sparse_matrix(sparse1, sparse2):
    sparse3 = dict(sparse1)
    for pair in sparse2:
        sparse3[pair] = sparse3.get(pair, 0) - sparse2[pair]
    return new_sparse_matrix(sparse3)  

def mul_sparse_matrix(sparse1, sparse2):
    sparse3 = dict()
    for (row1, col1) in sparse1:
        for(row2, col2) in sparse2:
            if col1 == row2:
                sparse3[row1, col2] = sparse3.get((row1, col2), 0) +\
                                      sparse1[row1, col1] * sparse2[row2, col2]
    return new_sparse_matrix(sparse3)

def is_diagonal(sparse):
    val = True
    for (row, col) in sparse:
        if row != col:
            val = False
            break
    return val

def is_empty(sparse):
    return False if sparse else True

def new_sparse_matrix(sparse):
    '''Funkcja usuwająca niepotrzebne pary tj. z wartościami równymi zero.'''
    newsparse = {(x, y): v for (x, y), v in sparse.items() if v != 0}
    return newsparse
