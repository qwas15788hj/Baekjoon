import sys
input = sys.stdin.readline

arr = [True] * 1000001
arr[0] = False
arr[1] = False
for i in range(2, len(arr)):
    if arr[i] == True:
        j = 2

        while (i * j) < len(arr):
            arr[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(1, len(arr), 2):
        if arr[i] and arr[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")