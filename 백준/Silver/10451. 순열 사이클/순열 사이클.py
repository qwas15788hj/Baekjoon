t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] -= 1

    visited = [False] * n

    answer = 0
    for i in range(n):
        if not visited[arr[i]]:
            visited[arr[i]] = True
            answer += 1

            nxt = arr[arr[i]]
            while not visited[nxt]:
                visited[nxt] = True
                nxt = arr[nxt]

    print(answer)