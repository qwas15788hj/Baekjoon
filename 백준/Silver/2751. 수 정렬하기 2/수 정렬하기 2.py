import sys
n = int(input())
arr = []
for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()
for i in arr:
    print(i)