
def gc_content(seq):
    count = 0 
    for i in seq:
        if i == 'G' or i == 'C':
            count += 1
    return (count / (len(seq)-4)) * 100 # len - 4 because seq will also have the 4-digit code of seq

def max_index(list):
    max = float('-inf')
    index = 0
    for i, j in enumerate(list):
        if j >= max:
            max = j
            index = i
    return index

def list2string(list):
    str = ''
    for i in list:
        str+=i
    return str

if __name__ == '__main__':
    with open('rosalind_gc.txt') as f:
        data = f.read()
        seq = data.split('>Rosalind_')
        dna = [i.replace('\n','') for i in seq]
    gc = []
    for i in dna:
        if i!= '':
            gc.append(gc_content(i))
    index = max_index(gc)
    print('Rosalind_'+str(dna[index + 1][:4])) # index + 1 because 1st element of list will be null
    print(gc[index])
