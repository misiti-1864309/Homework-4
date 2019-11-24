def FASTA_parse(file):
    strings = {}
    with open(file) as f:
        text = f.read()
        items = text.split('>')
    for item in items[1:]:
        item = item.split('\n')
        string_id = item.pop(0)
        strings[string_id] = ''.join(item)
    return strings

def revc(s):
    s = s[::-1]
    return s.translate(str.maketrans('ACGT','TGCA'))

res = []
string = list(FASTA_parse('rosalind_revp.txt').values())[0]
for i in range(len(string)):
    for j in range(12, 3, -1):
        if i+j <= len(string) and string[i:i+j] == revc(string[i:i+j]):
            res.append(' '.join(map(str, [i+1, j]))+'\n')
            break
            

with open('rosalind_revp_out.txt', 'w') as f:
    f.writelines(map(str, res))