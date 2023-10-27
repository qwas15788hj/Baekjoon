def solution(n, stations, w):
    answer = 0
    
    start = 0 # 시작 지점
    end = 0 # 끝 지점
    for i in range(len(stations)):
        if i == 0: # 첫 시작이면
            start = 1 # 1이 시작지점
        else: # 첫 시작 아니면
            start = stations[i-1] + w + 1 # 이전 기지국 끝부분 + 1 지점
        end = stations[i] - w - 1 # 현재 기지국의 시작지점 -1 지점
        
        answer += (end - start + 1) // (w * 2 + 1) # 시작과 끝지점 모두 전파 도달할 수 있는 최소 기지국
        if (end - start + 1) % (w * 2 + 1) != 0: # 나눠지지 않으면 1개 추가
            answer += 1
    
    # 마지막 예외처리
    start = stations[-1] + w + 1
    end = n
    if start <= end:
        answer += (end - start + 1) // (w * 2 + 1)
        if (end - start + 1) % (w * 2 + 1) != 0:
            answer += 1
    
    return answer