def solution(players, m, k):
    answer = 0
    
    server = 0 # 현재 시간에 증설된 서버 개수
    dic = dict()
    for i in range(len(players)):
        if i in dic:
            server -= dic[i]
            
        if (players[i]//m) > server:
            count = (players[i]//m) - server # 새로 개설해야 할 서버 개수
            dic[i+k] = count # dic[서버 끝나는 시간] = 개설된 수
            server += count # 서버 개수 증가
            answer += count
        
    return answer