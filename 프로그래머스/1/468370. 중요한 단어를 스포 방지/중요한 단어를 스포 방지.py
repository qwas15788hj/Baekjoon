def solution(message, spoiler_ranges):
    answer = 0
    
    message += " "
    n = len(message)
    m = len(spoiler_ranges)
    # 모든 스포일러 인덱스
    spoiler = dict()
    for s, e in spoiler_ranges:
        for i in range(s, e+1):
            spoiler[i] = 1
    
    spo, n_spo = [], []
    word = ""
    s, e = 0, 0
    for i in range(n-1):
        # 단어 종료 지점
        if message[i] != " " and message[i+1] == " ":
            word += message[i]
            e = i
            # 스포 단어인지 체킹
            flag = False
            for j in range(s, e+1):
                if j in spoiler:
                    flag = True
            if flag:
                spo.append(word)
            else:
                n_spo.append(word)
            
            # 새로 시작
            s = i+2
            e = 0
            word = ""
            
        # 중간단어
        if message[i] != " " and message[i+1] != " ":
            word += message[i]
    
    # 최종 스포일러 단어 개수 체크
    for s in spo:
        if s not in n_spo:
            answer += 1
            n_spo.append(s)
    
    return answer