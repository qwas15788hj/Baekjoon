from itertools import combinations_with_replacement, product

def solution(n, info):
    answer = [-1]
    gap = -1 #라이언, 어피치 점수 차
    
    #화살 n개 별 맞은 과녁
    arrows_list = list(combinations_with_replacement(range(0, 11), n))
    for arrows in arrows_list: #경우의 수 하나씩 체크
        lion_info = [0]*11
        for arrow in arrows:
            lion_info[10-arrow] += 1 #맞은 과녁 라이언 과녁에 추가, 낮은 점수부터 채워나가야 나중에 갱신 가능
        
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if info[i] == 0 and lion_info[i] == 0:  #둘다 해당 과녁에 쏜 게 없다면 패스
                continue
            elif info[i] >= lion_info[i]: #어피지가 쏜게 많거나 같다면
                apeach_score += 10-i #어피치 점수 증가
            else: #라이언이 더 많이 쏘면
                lion_score += 10-i #라이언 점수 증가
        
        if lion_score > apeach_score: #라이언 점수가 높다면
            if gap < lion_score-apeach_score: #최고 차이점보다 현재 차이점이 크다면
                gap = lion_score-apeach_score #갱신
                answer = lion_info #갱신
        
    return answer