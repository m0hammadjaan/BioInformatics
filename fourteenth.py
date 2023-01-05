with open('rosalind_cons.txt') as f:
    data = f.read()
    seq = data.split('>Rosalind_')
    line = [i.replace('\n','') for i in seq]
    dna = []
    for i in line:
        if i != '':
            dna.append(list(i[4:]))



profile = [[None] * len(dna[0]) for i in range(4)]



codon = [0] * 4

def clear_codon(codon):
    codon = [0] * 4
    return codon



A, C, T, G = 0, 0, 0, 0

for i in range(len(dna[0])):
    for j in range(len(dna)):
        if dna[j][i] == 'A':
            codon[0]+= 1
        if dna[j][i] == 'C':
            codon[1]+= 1
        if dna[j][i] == 'G':
            codon[2]+= 1
        if dna[j][i] == 'T':
            codon[3]+= 1

    for j in range(len(profile)):
        profile[j][i] = codon[j]

    codon = clear_codon(codon)

codon_dict = {
    0 : 'A',
    1 : 'C',
    2 : 'G',
    3 : 'T'
}



consensus = ''

def max_index(list):
    max = 0
    index = 0
    for i, j in enumerate(list):
        if j >= max:
            max = j
            index = i
    return index



for i in range(len(profile[0])):
    temp = []
    for j in range(len(profile)):
        temp.append(profile[j][i])
    consensus+= codon_dict[max_index(temp)]


with open('rosalind_cons_output.txt', 'w') as f:
    f.write(consensus)
    f.write('\n')
    for i in range(len(profile)):
        f.write(codon_dict[i]+': ')
        for j in profile[i]:
            f.write(str(j)+' ')
        f.write('\n')
