from itertools import combinations

def solution(relation):
    answer = []
    
    n = len(relation) # 로우 개수 (세로)
    m = len(relation[0]) # 컬럼 개수 (가로)
    arr = [set() for _ in range(m)] # 컬럼 개수 만큼 집합 배열 생성
    idx_list = [i for i in range(m)]
            
    store = []
    for i in range(1, m + 1): # 1 ~ m 까지
        for idx in list(combinations(idx_list, i)): # 컬럼별 조합
            dic = dict() # 딕셔너리 생성
            for j in range(n): # 한 로우 (한 줄) 마다
                word = "" # 단어 생성
                for now_idx in idx: # 현재 확인할 인덱스
                    word += relation[j][now_idx] # 현재 로우의 키
                if word not in dic: # 현재 로우의 키가 딕셔너리에 없다면
                    dic[word] = 1 # 생성
                    
            # 현재 idx 컬럼별 조합으로 딕셔너리가 다 채워졌다면
            if len(dic) == n:
                store.append(idx)
    
    
    for st in store:
        flag = True
        for i in range(1, len(st)):
            for now in list(combinations(st, i)):
                if now in store:
                    flag = False
                    break
            if flag == False:
                break
        
        if flag:
            answer.append(st)
                
                
    return len(answer)