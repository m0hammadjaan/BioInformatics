def longestCommonSubsequence(seq1, seq2):
    seq1 = '-' + seq1   
    seq2 = '-' + seq2
    scoreMatrix = [[0 for i in range(len(seq2))] for j in range(len(seq1))]
    Backtrack = [[0 for i in range(len(seq2))] for j in range(len(seq1))]
    for i in range(1, len(scoreMatrix)):
        scoreMatrix[i][0] = scoreMatrix[i - 1][0]
        Backtrack[i][0] = 1
    for j in range(1, len(scoreMatrix[0])):
        scoreMatrix[0][j] = scoreMatrix[0][j - 1]
        Backtrack[0][j] = 2
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            diagonal = scoreMatrix[i - 1][j - 1] + (1 if seq1[i] == seq2[j] else 0)
            down = scoreMatrix[i - 1][j]
            right = scoreMatrix[i][j - 1]
            scoreMatrix[i][j] = max([0, down, right, diagonal])
            if scoreMatrix[i][j] == 0:
                Backtrack[i][j] = 0
            elif scoreMatrix[i][j] == down:
                Backtrack[i][j] = 1
            elif scoreMatrix[i][j] == right:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4

    maxScore = float('-inf')
    index = (-1, -1)
    for i, row in enumerate(scoreMatrix):
        for j, value in enumerate(row):
            if value > maxScore:
                maxScore = value
                index = (i, j)

    seq1 = seq1[1:]
    i, j = index
    result = ''
    while Backtrack[i][j] != 0:
        if Backtrack[i][j] == 4:
            result = seq1[i - 1] + result
            i -= 1
            j -= 1
        elif Backtrack[i][j] == 2:
            j -= 1
        else:
            i -= 1
    return result

def main():
    try:
        with open('rosalind_lcsq.txt') as f:
            data = f.read()
            data = data.split('>Rosalind_')
            seq = [i[4:].replace('\n','') for i in data if i != '']
        s, t = seq
        LCS = longestCommonSubsequence(s, t)
        with open('rosalind_lcsq_output.txt', 'w') as f:
            f.write(LCS)
    except Exception as e:
        print(e)




if __name__ == '__main__':
    main()