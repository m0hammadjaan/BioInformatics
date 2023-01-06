def sequence(n): # O(n)
    return list(range(1, n+1))

def sequence_permutations(x): # O(n!)
    if len(x) == 0:
        return []
    if len(x) == 1:
        return [x]
    permutations = []
    for i in range(len(x)):
        element = x[i]
        remaining_elements = x[:i] + x[i+1:]
        for j in sequence_permutations(remaining_elements):
            permutations.append([element] + j)
    return permutations


with open('rosalind_perm.txt') as f:
    x = sequence(int(f.read()))
    y = sequence_permutations(x)
    print(len(y))
    for i in y:
        for j in i:
            print(j, end=' ')
        print()

