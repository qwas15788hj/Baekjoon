import sys
input = sys.stdin.readline

t = int(input())
arr = [1, 1, 2, 4, 8]
for i in range(5, 68):
    arr.append(arr[i-1] * 2 - arr[i-5])

for _ in range(t):
    n = int(input())
    print(arr[n])