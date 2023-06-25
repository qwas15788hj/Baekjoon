def solution(n,a,b):
    answer = 0
    
    while True:
        # a, b 중 작은 값이 홀수고, 큰 값이 짝수고, 큰 값 - 작은 값이 1일때 경기를 치름
        if min(a, b) % 2 == 1 and max(a, b) % 2 == 0 and max(a, b) - min(a, b) == 1:
            answer += 1 # + 1
            break # 종료
        a = a // 2 + a % 2 # a의 다음 번호 (몫 + 나머지)
        b = b // 2 + b % 2 # b의 다음 번호 (몫 + 나머지)
        answer += 1
    
    return answer