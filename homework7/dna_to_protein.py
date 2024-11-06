#File name dna_to_protein.py
def generate_sequence(length):
    #function that generates a DNA sequence
    #Inputing a nucleotide martix of variable length and returing a sequence of DNA
    nucleotide_matrix = [
        ['A', 'T', 'C', 'G'],
        ['C', 'G', 'A', 'T'],
        ['G', 'C', 'T', 'A'],
        ['T', 'A', 'G', 'C']
    ]
    
    DNA_sequence = ""
    
    #Go through lists and choose nucleotide
    for i in range(length):
       
        row = nucleotide_matrix[i % len(nucleotide_matrix)]
        
        # Select an element within the row using a column index that varies slightly
        column = (i // len(nucleotide_matrix)) % len(row)
        
        # Append the chosen nucleotide to the gene sequence
        DNA_sequence += row[column]
    
    return DNA_sequence


def transcribe_sequence(DNA_sequence):
    #function that produces an RNA sequence from the DNA sequence
    #initialize
    rna_sequence = ''

    #change T to U and append
    for nucleotide in DNA_sequence:
        if nucleotide == 'T':
            rna_sequence += 'U'
        else:
            rna_sequence += nucleotide
            
    return rna_sequence

def translate_sequence(rna_sequence):
    # Function that changes RNA sequence to a protein sequence
    # Codon chart
    codon_chart = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
        'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T',
        'ACG': 'T', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'GAU': 'D',
        'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UAU': 'Y', 'UAC': 'Y',
        'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop',
        'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G',
        'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'CAU': 'H', 'CAC': 'H'
    }
    
    # Initialize protein sequence
    protein_sequence = ''

    # Go over RNA sequence in steps of 3 (codon size)
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        
        # Check if the codon exists in codon_chart
        if codon in codon_chart:
            amino_acid = codon_chart[codon]
        else:
            amino_acid = 'X'
        
        # Stop translation if codon is a stop codon
        if amino_acid == 'Stop':
            return protein_sequence
        
        # Append the amino acid to the protein sequence
        protein_sequence += amino_acid
    
    return protein_sequence