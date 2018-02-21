def to_rna(dna_strand):
    dna_strand = list(dna_strand)
    for idx, item in enumerate(dna_strand):
        if item == "G":
            dna_strand[idx] = "C"
        elif item == "C":
            dna_strand[idx] = "G"
        elif item == "T":
            dna_strand[idx] = "A"
        elif item == "A":
            dna_strand[idx] = "U"
        elif item == "U":
            raise ValueError("Can't convert 'U' from a DNA to RNA")
        else:
            raise ValueError("Given data is invalid for convertion")
    return "".join(dna_strand)
