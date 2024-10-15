L = [12, 43, 56, 111, 98, 75]

L_strings = [str(num) for num in L]
num_str = ''.join(L_strings)

assert num_str == '1243561119875'
print(num_str)
