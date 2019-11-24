with open('rosalind_subs.txt') as f:
    string = f.readline().strip()
    sub = f.readline().strip()
loc = []
i = -1
while True:
    i = string.find(sub, i+1)
    if i == -1:
        break
    else:
        loc.append(i+1)
print(*loc)