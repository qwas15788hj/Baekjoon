t = int(input())
sosu = [True] * 1000001
sosu[0], sosu[1] = False, False
for i in range(2, int(1000001**0.5) + 1):
    if sosu[i]:
        for j in range(i*2, 1000001, i):
            sosu[j] = False

for _ in range(t):
    n = int(input())
    count = 0
    for i in range(2, n//2+1):
        if sosu[i] and sosu[n-i]:
            count += 1

    print(count)