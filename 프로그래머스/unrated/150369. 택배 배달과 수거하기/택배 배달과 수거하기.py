def solution(cap, n, deliveries, pickups):
    answer = 0 # 총 이동거리
    total_d = sum(deliveries) # 배달 남은 총 개수
    total_p = sum(pickups) # 픽업 남은 총 개수
    start_d = len(deliveries) - 1 # 배달 시작 지점 (맨 끝부터)
    start_p = len(pickups) - 1 # 픽업 시작 지점 (맨 끝부터)
    
    # 배달과 픽업이 끝 날때까지 무한 반복
    while total_d != 0 or total_p != 0:
        len_d = 0 # 현재 배달 가장 먼 거리 체크
        cap_d = cap # 현재 남은 택배 상자
        
        # 남은 배달이 있다면 시작 지점부터 맨 앞 집까지
        if total_d != 0:
            for i in range(start_d, -1, -1):
                if cap_d == 0: # 현재 남은 택배 상자가 없다면 종료
                    break
                if deliveries[i] != 0: # 해당 집에 배달을 해야한다면
                    if deliveries[i] > cap_d: # 집에 필요한 배달량이 남은 택배 상자보다 많다면
                        deliveries[i] -= cap_d # 해당 집에 모든 택배 상자 배달
                        total_d -= cap_d # 총 개수에서 빼기
                        cap_d = 0 # 현재 택배 상자 모두 소비
                        start_d = min(start_d, i) # 현재 집부터 다시 시작
                    else: # 남은 택배 상자가 많다면
                        cap_d -= deliveries[i] # 남은 택배 상자 빼기
                        total_d -= deliveries[i] # 총 개수에서 빼기
                        deliveries[i] = 0 # 해당 집에 배달 완료
                        start_d = min(start_d, i-1)
                    len_d = max(len_d, i+1) # 배달 이동 거리 갱신
        
        # 배달과 같은 원리로 픽업 계산
        len_p = 0
        cap_p = cap
        if total_p != 0:
            for i in range(start_p, -1, -1):
                if cap_p == 0:
                    break
                if pickups[i] != 0:
                    if pickups[i] > cap_p:
                        pickups[i] -= cap_p
                        total_p -= cap_p
                        cap_p = 0
                        start_p = min(start_p, i)
                    else:
                        cap_p -= pickups[i]
                        total_p -= pickups[i]
                        pickups[i] = 0
                        start_p = min(start_p, i-1)
                    len_p = max(len_p, i+1)
        
        if len_d == 0:
            answer += len_p * 2
        elif len_p == 0:
            answer += len_d * 2
        else:
            # 배달, 픽업 중 가장 먼 거리 * 2 더하기
            answer += max(len_d, len_p) * 2
            
    return answer