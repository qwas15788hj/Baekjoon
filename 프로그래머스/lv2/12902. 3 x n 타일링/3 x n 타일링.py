def solution(n):
    answer = [0, 3, 11] # 0, 2, 4 길이 일때 개수
    
    # 홀수면 불가능
    if n % 2 != 0:
        return 0
    
    # 3 ~ n을 2로 나눈 인덱스까지
    for i in range(3, n//2 + 1):
        # 점화식 : f(n) = f(n-2) * 3 + f(n-4) * 2 + f(n-6) * 2 + ... f(2) * 2 + 2
        answer.append((answer[-1] * 3 + sum(answer[:-1]) * 2 + 2) % 1000000007)
    
    return answer[-1] % 1000000007