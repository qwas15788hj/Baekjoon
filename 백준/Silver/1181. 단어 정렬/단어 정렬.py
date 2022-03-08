import sys

arr = []
n = int(sys.stdin.readline())

for i in range(n):
    arr.append(sys.stdin.readline().strip())
    
arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)