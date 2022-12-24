with open('rosalind_rna.txt') as f:
    dna = f.read()
    rna = ''

    for i in dna:
        if i == 'T':
            rna+= 'U'
        else:
            rna+= i
    print(rna)