def solution(A, B):
    answer = 0
    
    A.sort()  # A를 정렬
    B.sort()  # B를 정렬
    
    for a in A:
        # A에서 가장 작은 숫자를 선택
        # B에서 A의 현재 숫자보다 큰 숫자 중 가장 작은 숫자와 비교
        # 승점을 얻을 수 있다면 승점을 증가시키고 해당 숫자는 사용된 것으로 처리
        for b in B:
            if b > a:
                answer += 1
                B.remove(b)
                break
    
    return answer
