def solution(record):
    # 유저 딕셔너리 만들기 user_id: user_name / ex: uid1234: Prodo, uid4567: Ryan
    user_list = dict()
    # record 반복
    # 앞이 leave가 아니면 user_id: user_name으로 계속 초기화
    for r in record:
        if r.split()[0] != 'Leave':
            user_list[r.split()[1]] = r.split()[2]
        else:
            pass
    
    # 최종 user_list 딕셔너리를 이용하여 user_list[user_id]를 검색하여 user_name으로 출력
    result = []
    for r in record:
        if r.split()[0] == 'Enter':
            result.append(user_list[r.split()[1]] + "님이 들어왔습니다.")
        elif r.split()[0] == 'Leave':
            result.append(user_list[r.split()[1]] + "님이 나갔습니다.")

    return result