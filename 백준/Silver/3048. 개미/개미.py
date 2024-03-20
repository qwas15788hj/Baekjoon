n, m = map(int, input().split())
a = list(input())
b = list(input())
t = int(input())

ant = a[::-1] + b
for _ in range(t):
    for i in range(n+m-1):
        if (ant[i] in a) and (ant[i+1] in b):
            ant[i], ant[i+1] = ant[i+1], ant[i]
            if ant[i+1] == a[0]:
                break

print("".join(ant))