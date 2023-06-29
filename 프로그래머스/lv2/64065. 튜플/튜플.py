def solution(s):
    
    dic = dict() # 원소 등장 횟수 저장할 딕셔너리
    s = s.replace("{", "") # s에서 "{" 삭제
    s = s.replace("}", "") # s에서 "}" 삭제
    arr = list(s.split(",")) # 남은 s에서 ,를 기준으로 나누어 리스트 형태로 변환
    
    for i in range(len(arr)): # arr 반복
        if int(arr[i]) in dic: # int 형으로 변환한 arr 원소가 dic에 있다면
            dic[int(arr[i])] += 1 # 해당 원소 + 1
        else: # dic에 없다면
            dic[int(arr[i])] = 1 # 새로운 원소 추가
    
    answer = [0] * len(dic) # dic 길이만큼 answer 배열 선언
    
    for key, value in dic.items(): # 딕셔너리 dic에 저장된 key와 value를 뽑으며
        answer[value - 1] = key # 원소가 나온 갯수 - 1 인덱스에 원소 key 저장
        
    return answer[::-1] # 많이 나온 원소가 처음이므로 거꾸로