from itertools import product

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
a = list(product(data, repeat=m))
a.sort()

for i in a:
    print(*i)