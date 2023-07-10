from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    arr = list(permutations(dungeons, len(dungeons))) # 던전을 순열 리스트로 선언 
    for i in range(len(arr)): # 순열 리스트 반복
        dungeon = arr[i] # 현재 던전
        count = 0 # 탐험한 던전 수 선언
        now_k = k # 현재 던전 피로도 = 최초 피로도 k
        for j in range(len(dungeon)): # 현재 던전 돌면서
            if now_k >= dungeon[j][0]: # 현재 피로도가 현재 던전의 필요 피로도보다 크거나 같으면
                now_k -= dungeon[j][1] # 현재 피로도에서 던전 소모 피로도 빼고
                count += 1 # 탐험 성공
            else: # 현재 피로도가 현재 던전의 필요 피로도보다 작으면
                break # 종료
        
        answer = max(answer, count) # 탐험 던전 갱신
        
    return answer