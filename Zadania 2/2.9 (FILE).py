def copy_no_comments(infile_name, outfile_name):
    '''Funkcja wykonująca kopiowanie pliku, która pomija linie
    zaczynające się od znaku # (linie z komentarzami).'''
    infile = open(infile_name, 'r')
    outfile = open(outfile_name, 'w')
    for line in infile:
        if not line.startswith('#'):
            outfile.write(line)
    infile.close()
    outfile.close()

copy_no_comments('infile.txt', 'outfile.txt')
