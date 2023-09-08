from itertools import combinations # 조합 사용
from bisect import bisect_left # 이분탐색 사용

def solution(info, query):
    answer = []
    dic = dict() # key와 점수 저장할 딕셔너리 생성
    
    # info돌면서 dic 채우기
    for i in range(len(info)):
        now = info[i].split() # 현재 지원자의 정보
        key = now[:-1] # 현재 지원자의 점수를 뺀 정보
        score = now[-1] # 현재 지원자의 점수
        
        # 현재 지원자의 모든 key 조합 생성
        for j in range(5): # 최소 0개 ~ 최대 4개까지 (지원자 점수제거한 키)
            for c in combinations(key, j): # 지원자의 현재 key에서 j개 조합 구하기
                temp = "".join(c) # 구한 키
                if temp in dic: # 구한 키가 이미 dic에 있다면
                    dic[temp].append(int(score)) # dic에 해당 키에 지원자 점수 추가
                else: # 구한 키가 dic에 없다면
                    dic[temp] = [int(score)] # dic에 키와 점수 생성
    
    # 딕셔너리 돌면서 키에 해당하는 점수들 정렬
    for i in dic:
        dic[i].sort()
    
    # 쿼리 돌면서 지원자 수 구하기
    for q in query:
        q_now = q.split() # 현재 쿼리의 정보
        q_key = q_now[:-1] # 현재 쿼리의 점수를 뺀 정보
        q_score = q_now[-1] # 현재 쿼리의 점수
        
        # 점수 뺀 정보인 key에서 and 삭제
        while True:
            if "and" not in q_key:
                break
            q_key.remove("and")
            
        # 점수 뺀 정보인 key에서 - 삭제
        while True:
            if "-" not in q_key:
                break
            q_key.remove("-")
            
        # and와 -뺀 리스트를 합쳐서 쿼리의 최종 key 구하기
        q_key = "".join(q_key)
        
        # 구한 현재 쿼리 key가 딕셔너리에 있다면
        if q_key in dic:
            scores = dic[q_key] # 해당 쿼리 키의 점수 리스트
            if scores: # 점수가 있다면
                count = bisect_left(scores, int(q_score)) # 리스트 중 쿼리에서 원하는 점수 미만인 점수 개수
                answer.append(len(scores) - count) # 리스트 총 개수 - 미만 개수를 answer에 저장
        else: # 쿼리 key가 없거나, key가 있지만 점수가 없다면
            answer.append(0) # 0 저장
        
    return answer