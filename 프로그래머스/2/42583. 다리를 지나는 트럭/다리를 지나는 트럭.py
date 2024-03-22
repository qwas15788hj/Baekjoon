def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    total_weight = 0
    
    while total_weight != 0 or len(truck_weights) != 0:
        answer += 1
        
        total_weight -= bridge.pop(0)
        bridge.append(0)
        
        if len(truck_weights) != 0:
            if total_weight + truck_weights[0] <= weight:
                bridge[-1] = truck_weights.pop(0)
                total_weight += bridge[-1]
    
    return answer