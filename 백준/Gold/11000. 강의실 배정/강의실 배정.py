import heapq
import sys
input = sys.stdin.readline

n = int(input()) # n 입력
arr = [list(map(int, input().split())) for _ in range(n)] # 배열 입력
arr.sort() # 정렬

room = [] # 강의실 생성
heapq.heappush(room, arr[0][1]) # 우선순위 큐를 이용하여 강의실에 맨 처음 시작하는 강의의 종료 시간 저장

# 1번 인덱스 ~ 끝까지 체크
for i in range(1, len(arr)):
    if arr[i][0] < room[0]: # 현재 강의의 시작이 가장 처음 들어온(시작이 가장 빠른)강의의 끝 시간보다 작다면
        heapq.heappush(room, arr[i][1]) # 추가로 사용해야 함으로 현재 강의의 종료 시간 저장
    else: # 현재 강의의 시작 시간이 저장된 끝 시간보다 크면
        heapq.heappop(room) # 처음 들어온 강의가 끝났음으로 해당 강의실 사용 가능함으로 빼고
        heapq.heappush(room, arr[i][1]) # 현재 강의 종료 시간 저장

print(len(room))