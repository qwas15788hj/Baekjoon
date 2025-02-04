import sys
input = sys.stdin.readline

n = int(input())
arr = [True] * 2000001

arr[0] = False
arr[1] = False
for i in range(2, 2000001):
    if arr[i] == True:
        j = 2

        while (i * j) < 2000001:
            arr[i * j] = False
            j += 1

for i in range(n, 2000001):
    if arr[i] and str(i) == str(i)[::-1]:
        print(i)
        break