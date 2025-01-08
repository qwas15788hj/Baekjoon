import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

sosu = [False] * (n+1)
for i in range(2, n+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosu[i] = True

k_sosu = [1] * (n+1)
for i in range(2, n+1):
    if sosu[i] and i > k:
        for j in range(i, n+1, i):
            k_sosu[j] = 0

print(sum(k_sosu) - 1)