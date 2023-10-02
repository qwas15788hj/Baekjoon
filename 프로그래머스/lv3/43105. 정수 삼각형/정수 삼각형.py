def solution(triangle):
    
    for i in range(1, len(triangle)): # 2번째 줄 ~ 끝까지
        for j in range(i + 1): # 0 ~ i 행까지 체크
            if j == 0: # 현재 행이 가장 왼쪽인 j 이면, triangle[i][0]
                triangle[i][j] += triangle[i-1][j] # 해당 위치에 + 이전 열 같은 행 더해주기
            elif j == i: # 현재 행이 가장 오른쪽인 i 이면, triangle[i][-1]
                triangle[i][j] += triangle[i-1][-1] # 해당 위치에 + 이전 열 가장 마지막 행 더해주기
            else: # 현재 행이 가운데면
                # 해당 위치에 + (이전 열 현재 행 전, 이전 열 현재 행) 중 큰 값 더해주기
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1]) # 마지막 열에서 가장 큰 값 return