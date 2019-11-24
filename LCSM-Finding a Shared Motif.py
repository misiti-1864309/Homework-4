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

strings = FASTA_parse('rosalind_lcsm.txt')
strings = list(strings.values())

shortest_string = min(strings, key=len)
substring = ''
for i in range(len(shortest_string)):
    for j in range(i, len(shortest_string)+1):
        candidate = shortest_string[i:j]
        if len(candidate) > len(substring) and all(candidate in string for string in strings):
            substring = candidate

with open('rosalind_lcsm_out.txt', 'w') as f:
    f.write(substring)