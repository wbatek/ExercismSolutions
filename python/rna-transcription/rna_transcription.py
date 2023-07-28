def to_rna(dna_strand):
    map = {"G": "C",
           "C": "G",
           "T": "A",
           "A": "U"
           }
    rna = ''
    for x in dna_strand:
        rna += map[x]
    return rna
