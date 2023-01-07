def kmerComposition(nucleotideSeq, k):
    composition = {}
    for i in range(len(nucleotideSeq) - (k - 1)):
        kmer = nucleotideSeq[i:i+k]
        if kmer in composition:
            composition[kmer]+= 1
        else:
            composition[kmer] = 1
    return composition



# s = 'CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'


if __name__ == '__main__':
    with open('rosalind_kmer.txt') as f:
        data = f.read()
        seq = data.split('>Rosalind_')
        dna = seq[1][4:].replace('\n','')
    composition = kmerComposition(dna, 4)
    residue = list(composition.keys())
    residue.sort()


    for i in range(len(residue)):
        print(composition[residue[i]], end=' ')

    