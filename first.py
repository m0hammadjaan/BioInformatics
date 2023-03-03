with open('rosalind_ini.txt','r') as f:
    data = f.read()
    # data = list(data)
    A_Count = 0
    C_Count = 0
    T_Count = 0
    G_Count = 0
    for i in data:
        if i == 'A':
            A_Count += 1
        elif i == 'C':
            C_Count += 1
        elif i == 'T':
            T_Count += 1
        elif i == 'G':
            G_Count += 1
    print(A_Count, C_Count, G_Count, T_Count)
