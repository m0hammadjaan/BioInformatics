with open('rosalind_dna.txt') as f:
    dna = f.read()
    count_A = 0
    count_C = 0
    count_T = 0
    count_G =0
    for i in dna:
        if i == 'A':
            count_A+=1
        elif i == 'C':
            count_C+=1
        elif i == 'T':
            count_T+=1
        elif i == 'G':
            count_G+=1
    print(count_A,count_C,count_G,count_T)