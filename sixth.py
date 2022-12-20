with open('rosalind_hamm.txt') as f:
    seq = f.read().split('\n')
    seq_1, seq_2 = seq[0], seq[1]
    count = 0

    if(len(seq_1) == len(seq_2)):
        for i,j in enumerate(seq_1):
            if seq_2[i] != j:
                count+= 1

    print(count)