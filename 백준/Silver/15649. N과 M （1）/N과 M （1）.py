from itertools import permutations

n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
a = list(permutations(data, m))
a.sort()

for i in a:
    print(*i)