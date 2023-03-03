with open('codon_table.txt') as f:
    codon_table = {}
    lines = f.readlines()
    for line in lines:
        codon, protein = line.split()
        codon_table[codon] = protein


def protein(rna):
    i = 0
    codon = ''
    protein_str = ''
    for i in range(0,len(rna),3):
        codon = rna[i]+rna[i+1]+rna[i+2]
        if codon_table[codon] != 'Stop':
            protein_str+= codon_table[codon]
    return protein_str

with open('rosalind_prot.txt') as f:
    rna = f.read()



print(protein(rna))

