import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

arr.sort()
for i in range(1, n+1):
    arr[i] += arr[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print(arr[e] - arr[s-1])