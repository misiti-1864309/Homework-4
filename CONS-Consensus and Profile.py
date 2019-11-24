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

strings = FASTA_parse('rosalind_cons.txt')
P = [[], [], [], []]
c = []
for i in range(len(list(strings.values())[0])):
    A, C, G, T = 0, 0, 0, 0
    for s in strings.values():
        if s[i] == 'A':
            A += 1
        elif s[i] == 'C':
            C += 1
        elif s[i] == 'G':
            G += 1
        elif s[i] == 'T':
            T += 1
    P[0].append(A);P[1].append(C);P[2].append(G);P[3].append(T)
    max_nt = max(A,C,G,T)
    if A == max_nt:
        c.append('A')
    elif C == max_nt:
        c.append('C')
    elif G == max_nt:
        c.append('G')
    elif T == max_nt:
        c.append('T')
    
#print(''.join(c))
#print('A:', *P[0])
#print('C:', *P[1])
#print('G:', *P[2])
#print('T:', *P[3])
with open('rosalind_cons_out.txt', 'w') as f:
    f.write(''.join(c)+'\n')
    f.write('A: '+' '.join(map(str,P[0]))+'\n')
    f.write('C: '+' '.join(map(str,P[1]))+'\n')
    f.write('G: '+' '.join(map(str,P[2]))+'\n')
    f.write('T: '+' '.join(map(str,P[3]))+'\n')