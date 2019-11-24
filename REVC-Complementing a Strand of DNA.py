def revc(s):
    s = s[::-1]
    return s.translate(str.maketrans('ACGT','TGCA'))

with open('rosalind_revc.txt') as f:
    s = f.readline().strip()
with open('rosalind_revc_out.txt', 'w') as f:
    f.write(revc(s))