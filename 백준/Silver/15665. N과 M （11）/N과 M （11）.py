from itertools import product

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
a = list(product(data, repeat=m))
a = list(set(a))
a.sort()

for i in a:
    print(*i)