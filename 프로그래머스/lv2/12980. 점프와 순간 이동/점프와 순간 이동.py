def solution(n):
    answer = 0
    
    while n != 0: # n이 0일 때까지
        if n % 2 == 0: # n이 짝수면
            n /= 2 # n을 2로 나누기 (순간이동)
        else: # n이 홀수면
            n -= 1 # 1빼기
            answer += 1 # 1칸 점프
        
    return answer