def solution(record):
    answer = []
    
    dic = dict() # 유저 정보 담을 딕셔너리 / 유저아이디 : 유저닉네임 형태로 저장
    for message in record: # record 돌면서
        msg = message.split(" ") # 띄어쓰기 기준으로 나누기
        if len(msg) == 3: # 길이가 3인 enter와 change만 파악
            dic[msg[1]] = msg[2] # 딕셔너리에 유저아이디 = 유저닉네임으로 갱신
    
    for message in record: # record 돌면서
        msg = message.split(" ") # 띄어쓰기 기준으로 나누기
        if msg[0] == "Enter": # 맨 앞이 enter면
            answer.append(dic[msg[1]] + "님이 들어왔습니다.") # 딕셔너리에서 유저아이디를 통해 유저닉네임 파악
        elif msg[0] == "Leave": # 맨 앞이 leave면
            answer.append(dic[msg[1]] + "님이 나갔습니다.") # 딕셔너리에서 유저아이디를 통해 유저닉네임 파악
    
    return answer