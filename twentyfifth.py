with open('codon_table.txt') as f:
    codon_table = {}
    lines = f.readlines()
    for line in lines:
        codon, protein = line.split()
        codon_table[codon] = protein

def codonOccur():
    count = {}
    for k, v in codon_table.items():
        if not (v in count.keys()):
            count[v] = 0
        count[v]+= 1
    return count

def possibleRNA(proteinSeq):
    count = codonOccur()
    possible = count['Stop']
    for i in proteinSeq:
        possible*= count[i]
    return possible
    

if __name__ == '__main__':
    with open('rosalind_mrna.txt') as f:
        proteinSeq = f.read().strip()
        print(proteinSeq)
    print(possibleRNA(proteinSeq))