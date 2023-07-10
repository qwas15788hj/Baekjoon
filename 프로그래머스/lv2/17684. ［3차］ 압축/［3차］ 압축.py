def solution(msg):
    answer = []
    
    dic = dict() # 딕셔너리 생성
    for i in range(1, 27): # 알파벳 사전 생성
        dic[chr(i+64)] = i
        
    now = msg[0] # 현재 알파벳
    num = 27 # 딕셔너리에 저장될 번호
    for i in range(1, len(msg)): # 1 인덱스부터 끝까지
        nxt = msg[i] # 현재 부분이 다음 글자
        if now + nxt in dic: # 현재 알파벳과 다음 글자가 딕셔너리에 있다면
            now += nxt # 현재 알파벳 갱신
        else: # 현재 알파벳과 다음 글자가 딕셔너리에 없다면
            answer.append(dic[now]) # 현재 글자 출력
            dic[now + nxt] = num # 현재 글자 + 다음 글자 사전 추가
            num += 1 # 사전 번호 증가
            now = nxt # 현재 알파벳 갱신
    
    answer.append(dic[now]) # 마지막 글자 출력
    
    return answer