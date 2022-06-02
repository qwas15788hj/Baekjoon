import sys
input = sys.stdin.readline

sieve = [False, False] + ([True]*(1000000-1))
for i in range(2, int(1000001**0.5)+1):
    if sieve[i] == True:
        for j in range(i*2, 1000000+1, i):
            sieve[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    flag = False
    for i in range(3, len(sieve)):
        if sieve[i] and sieve[n-i]:
            print(f"{n} = {i} + {n-i}")
            flag = True
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")