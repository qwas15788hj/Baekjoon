def d(n):
    n = n + sum(map(int, str(n)))
    return n

no_selfnum = set()

for i in range(1, 10001):
    no_selfnum.add(d(i))

for i in range(1, 10001):
    if i not in no_selfnum:
        print(i)