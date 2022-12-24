dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
stop_codon = ['UAG', 'UGA', 'UAA']
dict = { 'A' : 'T', 'C' : 'G', 'T' : 'A', 'G' : 'C'}

def reverseComplement(dna):
    rev = ''
    for i in dna:
        rev+= dict[i]
    return rev[::-1]



def dna2rna(dna):
    rna = ''
    for i in dna:
        if i == 'T':
            rna+= 'U'
        else:
            rna+= i
    return rna


def seq_separator(rna):
    seq = []
    for i in range(len(rna)):
        temp = []
        if(rna[i:i+3]) == 'AUG':
            for j in range(i,len(rna),3):
                if rna[j:j+3] not in stop_codon:
                    temp.append(rna[j:j+3])
                else:
        
                    break
        if(temp != []):
            seq.append(temp)
        
        
    return seq
dna = reverseComplement(dna)
rna = dna2rna(dna)
# rna = rna[::-1]

seq = seq_separator(rna)


with open('codon_table.txt') as f:
    codon_table = {}
    lines = f.readlines()
    for line in lines:
        codon, protein = line.split()
        codon_table[codon] = protein
    
protein = []

for i in range(len(seq)):
    temp = ''
    for j in seq[i]:
        temp+= codon_table[j]
    protein.append(temp)
print(seq)
print(protein)

print('MLLGSFRLIPKETLIQVAGSSPCNLS' == 'MLLGSFRLIPKETLIQVAGSSPCNLS')