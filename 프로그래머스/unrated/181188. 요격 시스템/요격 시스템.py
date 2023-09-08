import heapq

def solution(targets):
    answer = 0 # 필요한 미사일의 총 개수
    
    targets.sort() # 정렬
    
    arr = []
    heapq.heappush(arr, targets[0][1]) # 우선순위 큐를 이용하여 맨 처음 타겟의 끝 지점 저장
    answer += 1 # 필요한 미사일 증가
    
    # 타겟 미사일 1번 인덱스부터 돌면서
    for i in range(1, len(targets)):
        if targets[i][0] < arr[0]: # 현재 타겟의 시작 지점이 배열의 맨 앞에 있는 끝 지점보다 작으면
            heapq.heappush(arr, targets[i][1]) # 해당 타겟과 함께 제거 가능함으로 현재 타겟만 저장
        else: # 현재 타겟의 시작 지점이 배열의 맨 앞에 있는 지점보다 크거나 같으면
            arr = [] # 해당 타겟과 함께 제거 불가능함으로 배열 새로 생성
            heapq.heappush(arr, targets[i][1]) # 현재 타겟 끝지점 저장
            answer += 1 # 필요 미사일 개수 증가
    
    return answer