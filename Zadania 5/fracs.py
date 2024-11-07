import math

def add_frac(frac1, frac2):
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError
    else:
        fracsum = [0, 0]
        fracsum[0] = frac1[0] * frac2[1] + frac1[1] * frac2[0]
        fracsum[1] = frac1[1] * frac2[1]
        gcd =  math.gcd(fracsum[0], fracsum[1])
        fracsum[0] /= gcd
        fracsum[1] /= gcd
        return minus(fracsum)      

def sub_frac(frac1, frac2):
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError
    else:
        fracsub = [0, 0]
        fracsub[0] = frac1[0] * frac2[1] - frac1[1] * frac2[0]
        fracsub[1] = frac1[1] * frac2[1]
        gcd =  math.gcd(fracsub[0], fracsub[1])
        fracsub[0] /= gcd
        fracsub[1] /= gcd
        return minus(fracsub)    

def mul_frac(frac1, frac2):
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError
    else:
        fracmul = [0, 0]
        fracmul[0] = frac1[0] * frac2[0]
        fracmul[1] = frac1[1] * frac2[1]
        fracmul = [fracit / math.gcd(fracmul[0], fracmul[1]) for fracit
                    in fracmul]
        return minus(fracmul)

def div_frac(frac1, frac2):
    if (frac1[1] == 0 or frac2[1] == 0 or frac2[0] == 0):
        raise ZeroDivisionError
    else:
        fracdiv = [0, 0]
        fracdiv[0] = frac1[0] * frac2[1]
        fracdiv[1] = frac1[1] * frac2[0]
        fracdiv = [fracit / math.gcd(fracdiv[0], fracdiv[1]) for fracit
                    in fracdiv]
        return minus(fracdiv)

def is_positive(frac):
    if frac[1] == 0:
        raise ZeroDivisionError
    else:
        return True if frac[0] * frac[1] > 0 else False    

def is_zero(frac):
    if frac[1] == 0:
        raise ZeroDivisionError
    else:
        return True if frac[0] == 0 else False

def cmp_frac(frac1, frac2):
    if (frac1[1] == 0 or frac2[1] == 0):
        raise ZeroDivisionError
    else:
        if frac1[0] * frac2[1] == frac2[0] * frac1[1]:
            return 0
        else:
            return 1 if frac1[0] * frac2[1] > frac2[0] * frac1[1] else -1

def frac2float(frac):
    if frac[1] == 0:
        raise ZeroDivisionError
    else:
        return float(frac[0] / frac[1])

def minus(frac):
    '''Funkcja zapewniająca poprawny zapis znaku ułamka, tj. znak minus stojący
    przy liczniku oraz zapobieganie występowania znaku minus jednocześnie przy
    liczniku i mianowniku.'''
    if frac[0] > 0 and frac[1] < 0:
        frac[1] = abs(frac[1])
        frac[0] *= -1
    if frac[0] < 0 and frac[1] < 0:
        frac[0] = abs(frac[0])
        frac[1] = abs(frac[1])
    return frac
