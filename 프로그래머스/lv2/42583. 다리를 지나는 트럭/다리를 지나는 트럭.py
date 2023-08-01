def solution(bridge_length, weight, truck_weights):
    answer = 0 # 경과 시간
    bridge = [0 for _ in range(bridge_length)] # 다리 길이 만큼 다리 배열 생성
    bridge_weight = 0 # 현재 다리 무게
    
    while bridge: # 다리 배열 원소 남으면 계속 반복
        answer += 1 # 1초 시간 경과
        bridge_weight -= bridge.pop(0) # 다리 배열 맨 앞(맨 먼저 나가는 트럭)빼며 무게에서 빼주기
        if truck_weights: # 들어와야하는 트럭이 남아있다면
            # 현재 다리 무게와 현재 순서인 트럭의 무게 합이 버틸 수 있는 무게보다 작거나 같으면
            if bridge_weight + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0)) # 다리 맨 끝에 트럭 들어오기
                bridge_weight += bridge[-1]
            else: # 무게보다 크면
                bridge.append(0) # 트럭 대신 그냥 0들어오기
    
    return answer