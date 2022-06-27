from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))
a = list(permutations(data, m))
a.sort()

for i in a:
    print(*i)