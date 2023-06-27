def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1): # left ~ right 까지
        answer.append(max(i//n, i%n) + 1) # 2차원 배열의 위치인 x, y를 구한 후, 그 중 큰 값에 + 1
        
    return answer