import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
# 양방향 그래프 초기화
arr = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, i = map(int, input().split())
    arr[a].append([b, i])
    arr[b].append([a, i])

answer = 0
# 모든 지역을 시작점으로 설정
for start in range(1, n+1):
    queue = []
    heappush(queue, [0, start]) # [누적 거리, 현재 위치]
    distance = [1e9] * (n+1)
    distance[start] = 0
    while queue:
        dist, now = heappop(queue) # 현재 위치, 누적 거리
        if distance[now] < dist:
            continue
        for nx, cost in arr[now]: # 다음 위치, 다음위치 까지의 거리
            # 누적 거리 + 다음위치까지 거리보다 < 다음위치까지의 저장된 거리가 크다면 거리 갱신
            if dist + cost < distance[nx]:
                distance[nx] = dist + cost
                heappush(queue, [dist+cost, nx])

    count = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            count += item[i-1]

    answer = max(answer, count)

print(answer)