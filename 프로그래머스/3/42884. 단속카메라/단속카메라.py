import heapq

def solution(routes):
    answer = 0
    
    routes.sort() # 경로 정렬
    
    arr = []
    heapq.heappush(arr, routes[0][1]) # 경로들 중 첫 번째의 끝 지점 저장
    answer += 1
    print(routes)
    for i in range(1, len(routes)):
        if routes[i][0] <= arr[0]: # 현재 경로의 시작점보다 < 배열에 있는 가장 작은 끝 지점이 크거가 같으면
            heapq.heappush(arr, routes[i][1]) # 하나의 카메라로 할 수 있으므로 현재 경로의 끝지점만 저장
        else: # 현재 경로의 시작점이 배열의 가장 작은 지점보다 크면 카메라 하나 더 사용해야함
            arr = []
            heapq.heappush(arr, routes[i][1])
            answer += 1
    
    return answer