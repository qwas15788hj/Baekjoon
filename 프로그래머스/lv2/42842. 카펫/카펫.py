def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(3, total): # 가로 길이
        for j in range(3, i+1): # 세로 길이
            if i * j > total: # 가로 * 세로가 총합보다 크면 세로 멈추고 가로 늘리기
                break
            # 가로 * 세로가 총합과 같고 (가로-2) * (세로-2)가 안쪽인 yellow와 같다면 정답
            if i * j == total and (i-2) * (j-2) == yellow:
                return [i, j]