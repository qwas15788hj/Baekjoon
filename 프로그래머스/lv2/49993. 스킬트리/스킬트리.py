def solution(skill, skill_trees):
    answer = 0
    
    for sk in skill_trees: # 스킬트리 반복
        idx = 0 # 현재 찍어야할 스킬의 인덱스 번호
        flag = True
        for s in sk: # 현재 스킬트리 반복
            if s in skill: # 현재 스킬이 skill 안에 있다면 idx와 비교
                now_idx = skill.index(s) # 현재 스킬의 idx 값
                if now_idx > idx: # 현재 스킬의 idx가 찍어야할 idx보다 크면 실패
                    flag = False
                    break
                else: # 현재 스킬의 idx가 찍어야할 idx보다 작거나 같으면 성공
                    idx += 1 # 찍어야할 스킬의 인덱스 번호 증가
            if flag == False:
                break
                
        if flag:
            answer += 1
            
    return answer