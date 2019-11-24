with open('rosalind_rna.txt') as f:
    t = f.readline()
with open('rosalind_rna_out.txt', 'w') as f:
    f.write(t.replace('T', 'U'))