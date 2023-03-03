def alphaPermLexf(alphabets, n, intermediate = '', result = []):
    if n == 0:
        result.append(intermediate)
    else:
        for i in alphabets:
            alphaPermLexf(alphabets, n-1, intermediate + i, result)
    return result

with open('rosalind_lexf.txt') as f:
    alphabets, n = f.readlines()
    n = int(n)
    string = [i for i in alphabets if (i != ' ' and i != '\n')]
    comb = alphaPermLexf(string, n)
    for i in comb:
        print(i)