def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower() # 소문자화
    str2 = str2.lower() # 소문자화
    
    a_dic = dict() # str1 중 문자 갯수 체크할 딕셔너리
    b_dic = dict() # str2 중 문자 갯수 체크할 딕셔너리
    a_set = set() # str1 중 문자 담을 집합
    b_set = set() # str2 중 문자 담을 집합
    
    for i in range(len(str1) - 1): # str1 돌면서
        if str1[i].isalpha() and str1[i+1].isalpha(): # 인덱스 2개가 둘다 알파벳이면
            a_set.add(str1[i:i+2]) # a 집합에 넣고
            if str1[i:i+2] in a_dic: # 딕셔너리에 있다면
                a_dic[str1[i:i+2]] += 1 # + 1
            else: # 없다면
                a_dic[str1[i:i+2]] = 1 # 추가
                
    for i in range(len(str2) - 1): # str2 돌면서
        if str2[i].isalpha() and str2[i+1].isalpha(): # 인덱스 2개가 둘다 알파벳이면
            b_set.add(str2[i:i+2]) # b 집합에 넣고
            if str2[i:i+2] in b_dic: # 딕셔너리에 있다면
                b_dic[str2[i:i+2]] += 1 # + 1
            else: # 없다면
                b_dic[str2[i:i+2]] = 1 # 추가
                
    if len(a_set) == 0 and len(b_set) == 0: # 두 집합 모두 공집합이면
        answer = 65536 * 1
    else: # 두 집합 모두 원소가 있다면
        inter = list(a_set & b_set) # 교집합
        union = list(a_set | b_set) # 합집합
        
        inter_count = 0 # 교집합 갯수
        for i in range(len(inter)): # 교집합 돌면서
            num = 1e9
            if inter[i] in a_dic: # 교집합 원소가 a 에 있다면
                num = min(num, a_dic[inter[i]]) # 최솟값 갱신
            if inter[i] in b_dic: # 교집합 원소가 b 에 있다면
                num = min(num, b_dic[inter[i]]) # 최솟값 갱신
            inter_count += num # 교집합 갯수 더하기
            
        union_count = 0 # 합집합 갯수
        for i in range(len(union)): # 합집합 돌면서
            num = 0
            if union[i] in a_dic: # 합집합 원소가 a 에 있다면
                num = max(num, a_dic[union[i]]) # 최솟값 갱신
            if union[i] in b_dic: # 합집합 원소가 b 에 있다면
                num = max(num, b_dic[union[i]]) # 최솟값 갱신
            union_count += num # 합집합 갯수 더하기
            
        answer = 65536 * inter_count // union_count # 정답 구하기
    
    return answer