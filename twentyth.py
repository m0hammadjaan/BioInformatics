def kmerComposition(nucleotideSeq, k):
    composition = {}
    for i in range(len(nucleotideSeq) - k - 1):
        kmer = nucleotideSeq[i:i+k]
        if kmer in composition:
            composition[kmer]+= 1
        else:
            composition[kmer] = 1
    return composition



# s = 'CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'


if __name__ == '__main__':
    
    composition = kmerComposition(s, 4)
    residue = list(composition.keys())
    residue.sort()
    print(residue)

    for i in range(len(residue)):
        print(composition[residue[i]], end=' ')