def delIntrons(seq, intron):
    for i in range(len(seq)):
        if seq[i:i+len(intron)] == intron:
            seq = seq[:i]+seq[i+len(intron):]
    return seq



def protein(rna):
    i = 0
    codon = ''
    protein_str = ''
    with open('codon_table.txt') as f:
        codon_table = {}
        lines = f.readlines()
        for line in lines:
            codon, protein = line.split()
            codon_table[codon] = protein
    for i in range(0,len(rna),3):
        codon = rna[i]+rna[i+1]+rna[i+2]
        if codon_table[codon] != 'Stop':
            protein_str+= codon_table[codon]
    return protein_str

def dna2rna(dna):
    rna = ''
    for i in dna:
        if i == 'T':
            rna+= 'U'
        else:
            rna+= i
    return rna

if __name__ == '__main__':
    with open('rosalind_splc.txt') as f:
        data = f.read()
        seq = data.split('>Rosalind_')
        dna = [i[4:].replace('\n','') for i in seq if i!='']


    sequence = dna[0]
    for i in range(1,len(dna)):
        sequence = delIntrons(sequence, dna[i])
    
    rna = dna2rna(sequence)
    print(protein(rna))

