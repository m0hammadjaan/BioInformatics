def alphaPermLexf(alphabets, n, intermediate = '', result = []):
    if n == 0:
        result.append(intermediate)
    else:
        for i in alphabets:
            alphaPermLexf(alphabets, n-1, intermediate + i, result)
    return result


if __name__ == '__main__':
    with open('rosalind_lexv.txt') as f:
        alphabets, n = f.readlines()
        n = int(n)
        string = [i for i in alphabets if (i != ' ' and i != '\n')]
    comb = alphaPermLexf(string, n)
    temp = []
    for i in comb:
        for j in range(len(i)):
            if i[:j+1] not in temp:
                temp.append(i[:j+1])

    with open('rosalind_lexv_output.txt','w') as f:
        for i in  temp:
            f.write(i)
            f.write('\n')
