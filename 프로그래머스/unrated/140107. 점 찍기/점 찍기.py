def solution(k, d):
    answer = 0
    
    # x 기준 0 ~ d까지 k 증가
    # x축 기준으로 y축이 몇개가 존재하는지 찾으면 됨
    # 2중 for문 사용시 시간 초과
    for x in range(0, d+1, k):
        # y축 값 구하기
        y = (d**2 - x**2) ** 0.5 # x^2 + y^2 = d // => y = (d^2 - x^2)^0.5
        answer += y//k + 1 # k만큼 증가하기에 나온 y최대값//k + 1 (0 위치)
            
    return answer