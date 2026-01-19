n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(k):
    p = [0] * n
    for i in range(n):
        p[d[i]-1] = s[i]
    s = p

print(*p)