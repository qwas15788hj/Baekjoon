import sys
from collections import deque
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
x -= 1
y -= 1
start, end = [], []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    start.append([x1-1, y1-1])
    end.append([x2-1, y2-1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = [False] * m

# 태울 승객 찾는 함수
def find_start(a, b):
    t_queue = deque()
    t_queue.append([a, b])
    t_visited = [[1e9] * n for _ in range(n)]
    t_visited[a][b] = 0
    while t_queue:
        ta, tb = t_queue.popleft()
        for k in range(4):
            nta, ntb = ta + dx[k], tb + dy[k]
            if 0 <= nta < n and 0 <= ntb < n and arr[nta][ntb] == 0 and t_visited[nta][ntb] == 1e9:
                t_queue.append([nta, ntb])
                t_visited[nta][ntb] = t_visited[ta][tb] + 1

    target_x, target_y, target_dist = 1e9, 1e9, 1e9
    for k in range(m):
        if not flag[k]:
            i, j = start[k][0], start[k][1]
            if t_visited[i][j] < target_dist:
                target_x, target_y, target_dist = i, j, t_visited[i][j]
            elif t_visited[i][j] == target_dist:
                if i < target_x:
                    target_x, target_y, target_dist = i, j, t_visited[i][j]
                elif i == target_x and j < target_y:
                    target_x, target_y, target_dist = i, j, t_visited[i][j]

    return target_x, target_y, target_dist

# 도착 지점 최단 거리 찾는 함수
def find_end(a, b, idx):
    t_queue = deque()
    t_queue.append([a, b])
    t_visited = [[1e9] * n for _ in range(n)]
    t_visited[a][b] = 0
    while t_queue:
        ta, tb = t_queue.popleft()
        if ta == end[idx][0] and tb == end[idx][1]:
            return ta, tb, t_visited[ta][tb]
        for k in range(4):
            nta, ntb = ta + dx[k], tb + dy[k]
            if 0 <= nta < n and 0 <= ntb < n and arr[nta][ntb] == 0 and t_visited[nta][ntb] == 1e9:
                t_queue.append([nta, ntb])
                t_visited[nta][ntb] = t_visited[ta][tb] + 1

    return -1, -1, 1e9

while True:
    if False not in flag:
        break

    # 승객 태우러 가는 로직
    x, y, dist = find_start(x, y)
    fuel -= dist
    if fuel < 0:
        break

    # 도착 지점 가는 로직
    idx = start.index([x, y])
    x, y, dist = find_end(x, y, idx)
    fuel -= dist
    if fuel < 0:
        break
    else:
        fuel += dist*2
        flag[idx] = True

print(max(-1, fuel))