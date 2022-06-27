from itertools import combinations_with_replacement

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
a = list(combinations_with_replacement(data, m))
a = list(set(a))
a.sort()

for i in a:
    print(*i)