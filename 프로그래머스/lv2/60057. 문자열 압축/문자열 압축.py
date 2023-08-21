def solution(s):
    answer = len(s) # 초기 값 : 문자 1개 단위로 잘랐을 경우 (최소)
    
    # 압축 단어 개수 만큼 돌리기 1 ~ 최대 길이 s만큼
    for i in range(1, len(s) + 1):
        pre = s[:i] # 압축 단어
        count = 0 # 압축 단어가 몇번 등장하였는지
        word = "" # 현재 최종 단어
        # 처음 ~ 끝까지, 압축 개수 i 만큼 증가
        for j in range(0, len(s) + i, i):
            now = s[j : j + i] # 현재 단어 j ~ j+i까지
            if pre == now: # 이전 압축 단어와 현재 단어가 같다면
                count += 1 # 카운트 증가
            else: # 다르다면
                if count > 1 : # 이전 압축 단어가 2번 이상 등장했다면
                    word = word + str(count) + pre # 카운트까지 하여 단어 재생성
                else: # 이전 압축 단어가 1번 등장했을 경우
                    word = word + pre # 단어만 추가
                    
                pre = now # 현재 단어를 이전 압축 단어로 변경
                count = 1 # 카운트 1로 초기화
        
        # 현재 i 길이 만큼 단어 압축 수행을 마쳤다면 answer와 완성된 word 길이 비교
        if answer > len(word):
            answer = len(word)
            
    return answer