from itertools import combinations
from collections import deque

arr = [list(input()) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
comb = list(combinations(range(25), 7))
# 모든 그룹
for com in comb:
    s_cnt, y_cnt = 0, 0
    # 한 그룹 체크
    for i in range(len(com)):
        # oo파 인원 체크
        if arr[com[i]//5][com[i]%5] == 'S':
            s_cnt += 1
        else:
            y_cnt += 1

    # 임도연 파가 4명 이상이면 종료
    if y_cnt >= 4:
        continue

    # 같은 한 그룹이 모두 인접하는지 체크
    count = 1
    queue = deque([])
    queue.append(com[0])
    visited = [False] * 25
    visited[com[0]] = True
    while queue:
        idx = queue.popleft()
        x, y = idx//5, idx%5
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            n_idx = nx * 5 + ny
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[n_idx] and n_idx in com:
                queue.append(n_idx)
                visited[n_idx] = True
                count += 1

    if count == 7:
        answer += 1

print(answer)