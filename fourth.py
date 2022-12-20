with open('rosalind_rna.txt') as f:
    dna = f.read()
    # dict = { 'A' : 'U', 'C' : 'G', 'T' : 'A', 'G' : 'C'}
    rna = ''

    for i in dna:
        if i == 'T':
            rna+='U'
        else:
            rna+=i
    print(rna)