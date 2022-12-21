def motifs(seq,sub_seq):
    index = []
    for i in range(len(seq)):
        if seq[i:i+len(sub_seq)] == sub_seq:
            index.append(i+1)
    return index


with open('rosalind_subs.txt') as f:
    seq, sub_seq = f.readlines()


print(motifs(seq,sub_seq))
