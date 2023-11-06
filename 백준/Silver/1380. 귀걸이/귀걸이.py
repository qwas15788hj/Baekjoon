t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break

    arr = []
    for _ in range(n):
        arr.append(input())

    visited = [0]*n
    for _ in range(2*n-1):
        a, b = map(str, input().split())
        visited[int(a)-1] += 1

    for i in range(n):
        if visited[i] == 1:
            print(t, arr[i])