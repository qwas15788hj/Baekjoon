from collections import deque

arr = []
for _ in range(4):
    wheel = list(input())
    queue = deque([])
    for w in wheel:
        queue.append(w)
    arr.append(queue)

k = int(input())
command = []
for _ in range(k):
    a, b = map(int, input().split())
    command.append([a, b])

for i, d in command:
    i -= 1

    # 회전 방향 체크
    dire = [0] * 4
    dire[i] = d
    for l in range(i-1, -1, -1):
        if arr[l][2] != arr[l+1][6]:
            dire[l] = -dire[l+1]
        else:
            break
    for r in range(i+1, 4):
        if arr[r][6] != arr[r-1][2]:
            dire[r] = -dire[r-1]
        else:
            break

    # 회전
    for j in range(4):
        if dire[j] == 1:
            arr[j].appendleft(arr[j].pop())
        if dire[j] == -1:
            arr[j].append(arr[j].popleft())

answer = 0
for i in range(4):
    if arr[i][0] == '1':
        answer += 2**i

print(answer)