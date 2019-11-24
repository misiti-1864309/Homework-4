with open('rosalind_dna.txt') as f:
    s = f.readline()
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))