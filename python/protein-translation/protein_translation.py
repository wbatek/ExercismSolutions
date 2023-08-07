from textwrap import wrap

codons = {
    ("AUG"): "Methionine",
    ("UUU", "UUC"): "Phenylalanine",
    ("UUA", "UUG"): "Leucine",
    ("UCU", "UCC", "UCA", "UCG"): "Serine",
    ("UAU", "UAC"): "Tyrosine",
    ("UGU", "UGC"): "Cysteine",
    ("UGG"): "Tryptophan",
    ("UAA", "UAG", "UGA"): "STOP"
}

item = lambda x: [z for y, z in codons.items() if x in y][0]


def proteins(strand):
    result = []
    for current in wrap(strand, 3):
        if item(current) == 'STOP':
            break
        result.append(item(current))
    return result
