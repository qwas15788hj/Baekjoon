from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
a = list(combinations(data, m))
a.sort()

for i in a:
    print(*i)