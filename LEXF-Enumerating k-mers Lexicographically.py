from itertools import product

with open('rosalind_lexf.txt') as f:
    A = f.readline().split()
    n = int(f.readline().strip())

with open('rosalind_lexf_out.txt', 'w') as f:
    for i in product(A, repeat=n):
        f.write(''.join(i)+'\n')