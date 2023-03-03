def sorted(list):
    for i in range(len(list)):
        sort = False
        for j in range(1, len(list) - i - 1):
            if len(list[i]) > len(list[j]):
                list[i], list[j] = list[j], list[i]
                sort = True
            if not sort:
                break
    return list

def sharedMotif(seq):
    seq = sorted(seq)
    shortest = seq[0]
    remaining = seq[1:]
    motif = ''
    for i in range(len(shortest)):
        for j in range(i, len(shortest)):
            m = shortest[i:j+1]
            matched = False
            for k in remaining:
                if m in k:
                    matched = True
                else:
                    matched = False
                    break
            if matched and len(m) > len(motif):
                motif = m
    return motif


if __name__ == '__main__':
    with open('rosalind_lcsm.txt') as f:
        data = f.read()
        seq = data.split('>Rosalind_')
        seq = [i[4:].replace('\n','') for i in seq if(i != '')]
    # list = ['ABCD', 'ABC', 'ABCDE']
    print(sharedMotif(seq))











