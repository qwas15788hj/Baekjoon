def solution(land):
    
    for i in range(1, len(land)): # 1 ~ 끝까지 반복하며
        # 현재 행의 현재 열의 최대값 = 이전 행의 현재 열을 뺀 나머지 열 중 가장 큰 값을 더함
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3]) # i행 0열 = i-1행 0열을 뺀 나머지 열 중 큰 값
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3]) # i행 1열 = i-1행 1열을 뺀 나머지 열 중 큰 값
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3]) # i행 2열 = i-1행 2열을 뺀 나머지 열 중 큰 값
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2]) # i행 3열 = i-1행 3열을 뺀 나머지 열 중 큰 값
    
    return max(land[-1]) # 마지막 행 중 가장 큰 값