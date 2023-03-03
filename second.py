from Bio import Entrez
with open('rosalind_gbk.txt') as f:
    data = f.readlines()

    Entrez.email = "janmuhammad2050@gmail.com"

    query = f'"{data[0]}"[Organism] AND "{data[1]}"[PDAT] : "{data[2]}"[PDAT]'

    handle = Entrez.esearch(db="nucleotide", term = query)

    record = Entrez.read(handle)

    print(record['Count'])

    handle.close()