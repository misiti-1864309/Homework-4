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
        
strings = FASTA_parse('rosalind_gc.txt')
GC_max = 0
for string_id, string in strings.items():
    GC = (string.count('G') + string.count('C')) / len(string) * 100
    if GC > GC_max:
        id_max, GC_max = string_id, GC
print(id_max); print(GC_max)