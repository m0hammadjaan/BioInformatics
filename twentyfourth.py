def splicedMotif(seq):
    s = seq[0]
    t = seq[1]
    indices = []
    index = 0
    x = True
    for i in range(len(t)):
        for j in range(index,len(s)):
            index+= 1
            if t[i] == s[j]:
                indices.append(index)
                break
    return indices

if __name__ == '__main__':
    with open('rosalind_sseq.txt') as f:
        data = f.read()
        seq = data.split('>Rosalind_')
        seq = [i[4:].replace('\n','') for i in seq if i != '']
    for i in splicedMotif(seq):
        print(i, end=' ')
