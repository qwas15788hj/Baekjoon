from collections import deque

n, k = map(int, input().split())

queue = deque([])
visited = [-1] * 100001
queue.append(n)
visited[n] = -2 # 시작지점 -2로 체크, 0으로 하면 수빈이가 0에서 시작하는 시작점을 역추적 할 수 없음
while queue:
    x = queue.popleft()
    if x == k:
        break

    if 0 <= x+1 < 100001 and visited[x+1] == -1:
        queue.append(x+1)
        visited[x+1] = x
    if 0 <= x-1 < 100001 and visited[x-1] == -1:
        queue.append(x-1)
        visited[x-1] = x
    if 0 <= x*2 < 100001 and visited[x*2] == -1:
        queue.append(x*2)
        visited[x*2] = x

answer = [k]
while True:
    prev = visited[k]
    if prev == -2:
        break
    answer.append(prev)
    k = prev

print(len(answer)-1)
print(*answer[::-1])