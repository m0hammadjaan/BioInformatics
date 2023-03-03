with open('rosalind_revc.txt') as f:
    dna = f.read()
    dict = { 'A' : 'T', 'C' : 'G', 'T' : 'A', 'G' : 'C'}
    complement = ''
    reverse_complement = ''
    for i in dna:
        if i in dict.keys():
            complement+= dict[i]    

    reverse_complement = complement[::-1]

    print(reverse_complement)