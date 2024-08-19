n = int(input())
arr = [input() for _ in range(n)]
k = len(arr[0])
for i in range(1, k+1):
    s = set()
    for j in range(n):
        s.add(arr[j][k-i:])
    if len(s) == n:
        print(i)
        break