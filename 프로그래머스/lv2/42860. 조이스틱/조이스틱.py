def solution(name):
    answer = 0 # 총 수
    count = 0 # A가 아닌 문자의 수
    
    # 각 자리 문자가 A가 되기 위한 최소 수 구하기
    for i in name:
        answer += min(ord(i) - 65, 91 - ord(i)) # A에서 올리거나, 내린 것 중 작은 작업으로 진행
        if i != "A": # A가 아닌 문자 수 찾기
            count += 1
    
    # 오른쪽먼저 갔다가 왼쪽으로
    total_move = 1e9
    for i in range(len(name)):
        move = 0
        cnt = 0
        if name[0] != "A":
            cnt += 1
        for j in range(1, i+1):
            if cnt == count:
                break
            move += 1
            if name[j] != "A":
                cnt += 1
        # 다 찾으면 종료
        if cnt == count:
            total_move = min(total_move, move)
        else: # 다 못찾았으면 돌아가고 뒤로
            move += i
            for j in range(len(name)-1, i, -1):
                if cnt == count:
                    break
                move += 1
                if name[j] != "A":
                    cnt += 1
            total_move = min(total_move, move)
    
    # 왼쪽으로 갔다가 오른쪽으로
    for i in range(1, len(name)):
        move = 0
        cnt = 0
        if name[0] != "A":
            cnt += 1
        for j in range(-1, -(i+1), -1):
            if cnt == count:
                break
            move += 1
            if name[j] != "A":
                cnt += 1
        # 다 찾으면 종료
        if cnt == count:
            total_move = min(total_move, move)
        else: # 다 못찾았으면 돌아가고 뒤로
            move += i
            for j in range(1, len(name)-i):
                if cnt == count:
                    break
                move += 1
                if name[j] != "A":
                    cnt += 1
            total_move = min(total_move, move)
    
    if total_move != 1e9:
        answer += total_move
        
    return answer