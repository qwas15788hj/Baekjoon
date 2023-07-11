import heapq

def solution(scoville, K):
    answer = 0 # 카운트
    arr = [] # 힙 배열
    
    for i in scoville: # 힙 배열 채우기
        heapq.heappush(arr, i)
    
    while arr[0] < K: # 가장 작은 매운 맛이 K보다 작을 때 반복
        num = heapq.heappop(arr) + heapq.heappop(arr) * 2 # 가장 작은 것 + 2번째로 작은 것 * 2
        heapq.heappush(arr, num) # 힙 배열에 넣기
        answer += 1 # 카운트 증가
        if len(arr) == 1 and arr[0] < K: # 배열 길이가 1이고, K보다 작으면 실패
            answer = -1
            break
    
    return answer	