from collections import deque

def solution(cards):
    answer = []
    
    n = len(cards) # 총 카드 개수
    visited = [False] * n # 카드를 뽑았는지 체크
    # 카드 마다 돌면서
    for i in range(len(cards)):
        # 현재 카드 번호를 한번도 안뽑았다면
        now = cards[i] - 1
        if not visited[now]:
            count = 0 # 카운트
            while visited[now] == False: # 현재 뽑은 카드의 번호를 한번도 안뽑았다면 계속 진행
                count += 1 # 카운트 증가
                visited[now] = True # 현재 뽑은 카드 번호 체크
                now = cards[now] - 1 # 현재 뽑은 카드 번호의 다음 카드 번호를 now로 지정하여 계속
            answer.append(count) # 카운트 배열에 저장
    
    answer.sort(reverse=True) # 높은 순으로 내림차순
    # 1그룹밖에 없다면 0 return
    if len(answer) == 1:
        return 0
    
    return answer[0] * answer[1]