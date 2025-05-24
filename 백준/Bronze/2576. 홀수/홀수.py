odd, total = 1e9, 0
for _ in range(7):
    n = int(input())
    if n%2 != 0:
        total += n
        odd = min(odd, n)

if odd != 1e9:
    print(total)
    print(odd)
else:
    print(-1)