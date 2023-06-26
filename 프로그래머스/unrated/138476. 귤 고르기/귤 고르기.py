from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # 배열 요소 각각의 갯수를 배열로 만드는 Counter 라이브러리 사용
    arr = Counter(tangerine).most_common()
    count = 0 # 고를 과일 수
    
    for i in range(len(arr)):
        if count >= k: # 갯수가 k 이상이면 끝
            break
        count += arr[i][1] # 갯수 증가
        answer += 1 # 종류 증가
    
    return answer