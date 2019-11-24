with open('rosalind_lgis.txt') as f:
    n = int(f.readline().strip())
    pi = list(map(int, f.readline().split()))

def LIS_LDS(v, n):
    lis, lds  = [1] * n, [1] * n
    prev_i, prev_d = [], []
    for i in range(n):
        prev_i.append(i)
        prev_d.append(i)
    for i in range(1, n):
        for j in range(i):
            if v[i] > v[j] and lis[i] <= lis[j]:
                lis[i] = lis[j] + 1
                prev_i[i] = j
            if v[i] < v[j] and lds[i] <= lds[j]:
                lds[i] = lds[j] + 1
                prev_d[i] = j
    max_i, max_d = max(lis), max(lds)
    index_i, index_d = lis.index(max_i), lds.index(max_d)
    LIS, LDS = [v[index_i]], [v[index_d]]
    while index_i != prev_i[index_i]:
        index_i = prev_i[index_i]
        LIS.append(v[index_i])
    while index_d != prev_d[index_d]:
        index_d = prev_d[index_d]
        LDS.append(v[index_d])
    return LIS[::-1], LDS[::-1]

LIS, LDS = LIS_LDS(pi, n)
with open('rosalind_lgis_out.txt', 'w') as f:
    f.write(' '.join(map(str, LIS))+'\n')
    f.write(' '.join(map(str, LDS)))