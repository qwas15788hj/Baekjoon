n, m = map(int, input().split())
arr = []
for _ in range(n):
    sub = []
    s = input()
    for i in s:
        sub.append(i)
    arr.append(sub)

visited = [[False] * m for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == "-" and not visited[i][j]:
            answer += 1
            idx = 0
            while True:
                if j + idx >= m:
                    break
                if arr[i][j+idx] == "|" or visited[i][j+idx]:
                    break
                visited[i][j+idx] = True
                idx += 1

for i in range(m):
    for j in range(n):
        if arr[j][i] == "|" and not visited[j][i]:
            answer += 1
            idx = 0
            while True:
                if j + idx >= n:
                    break
                if arr[j+idx][i] == "-" or visited[j+idx][i]:
                    break
                visited[j+idx][i] = True
                idx += 1

print(answer)