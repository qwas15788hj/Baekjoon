n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

basket = [i for i in range(n+1)]
for i in range(m):
    a, b = arr[i][0], arr[i][1]
    basket[a], basket[b] = basket[b], basket[a]

print(*basket[1:])