def to_rna(dna_strand):
    mapping = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    if any(letter not in mapping for letter in dna_strand):
        raise ValueError("DNA strand must consist of only G, C, T or A")
    return "".join([mapping.get(item, item) for item in dna_strand])
    
    
if __name__ == "__main__":
    print(to_rna("ACGTGGTCTTAA"))
