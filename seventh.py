def transition(seq_1,seq_2):
    trans = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            if seq_1[i] in 'CT' and seq_2[i] in 'CT':
                trans+= 1
            elif seq_1[i] in 'AG' and seq_2[i] in 'AG':
                trans+= 1
    return trans

def transversion(seq_1,seq_2):
    transv = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            if seq_1[i] in 'CT' and seq_2[i] in 'AG':
                transv+= 1
            elif seq_1[i] in 'AG' and seq_2[i] in 'CT':
                transv+= 1
    return transv


seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
seq2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'



print(transition(seq1,seq2)/transversion(seq1,seq2))