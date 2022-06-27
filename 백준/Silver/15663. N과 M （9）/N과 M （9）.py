from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
a = list(permutations(data, m))
a = list(set(a))
a.sort()

for i in a:
    print(*i)