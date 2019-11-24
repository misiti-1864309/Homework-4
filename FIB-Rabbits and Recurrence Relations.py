d = {0: 0, 1: 1}
def fib(n, k):
    if n in d.keys():
        return d[n]
    else:
        d[n] = fib(n-1, k) + k*fib(n-2, k)
        return d[n]

with open('rosalind_fib.txt') as f:
    n, k = map(int, f.readline().split())

print(fib(n,k))