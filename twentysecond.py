def reverseComplement(seq):
    complement = ''
    for i in seq:
        if i == 'A':
            complement+= 'T'
        elif i == 'C':
            complement+= 'G'
        elif i == 'T':
            complement+= 'A'
        else:
            complement+= 'C'
    return complement[::-1]

def isPalindrome(seq):
    return seq == reverseComplement(seq)

def restrictionSites(seq):
    dict = []
    revCompl = reverseComplement(seq)
    for i in range(4, 13):
        for j in range(0, len(seq) - i + 1):
            str = seq[j:j+i]
            if isPalindrome(seq[j:j+i]):
                dict.append((j+1, i))
    return dict


if __name__ == '__main__':
    with open('rosalind_revp.txt') as f:
        data = f.read()
        seq = data.split('>Rosalind_')
        dna = seq[1][4:].replace('\n','')
    output = restrictionSites(dna)
    for i in output:
        start, length = i
        print(start, length)
 