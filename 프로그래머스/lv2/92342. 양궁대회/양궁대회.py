from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1] # 최초 -1로 생성
    gap = -1 # 어피치와 라이언의 점수 차이, 초기 -1로 생성
    
    # 라이언이 n발을 맞출 수 있는 모든 경우
    arrows_list = list(combinations_with_replacement(range(0, 11), n))
    # 경우의 수를 돌면서
    for arrows in arrows_list:
        lion = [0] * 11 # 라이언의 현재 과녁
        for arrow in arrows: # 라이언 과녁에 추가
            lion[10 - arrow] += 1 # 높은 점수부터 확인해야 나중에 같은 점수여도 낮은 수가 많아 갱신 가능
        
        apeach_score, lion_score = 0, 0 # 어피치와 라이언 각자의 점수
        # 과녁 돌면서
        for i in range(11):
            if info[i] == 0 and lion[i] == 0: # 현재 과녁에 어피치와 라이언이 둘다 못쐈으면 무시
                continue
            elif info[i] >= lion[i]: # 현재 과녁에 어피치가 라이언과 같거나 더 많이 쐈다면
                apeach_score += 10 - i # 어피치가 해당 점수 획득
            else: # 현재 과녁에 라이언이 더 많이 쐈다면
                lion_score += 10 - i # 라이언이 점수 획득
        
        if lion_score > apeach_score: # 라이언 점수가 어피치의 점수보다 크면
            if gap < lion_score - apeach_score: # 두 점수 차가 gap보다 크면
                gap = lion_score - apeach_score # gap 점수 갱신
                answer = lion # 현재 라이언 과녁으로 갱신
            
    return answer