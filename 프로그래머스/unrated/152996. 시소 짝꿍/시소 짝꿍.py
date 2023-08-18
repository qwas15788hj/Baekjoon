from collections import Counter
def solution(weights):
    answer = 0
    
    # 몸무게 별 사람 수
    count = Counter(weights)
    
    # 몸무게, 사람 수 하나씩 돌면서 1:1 같은 몸무게 사람 찾기
    for w, c in count.items():
        if c >= 2: # 같은 몸무게가 2명 이상이면
            answer += (c * (c-1)) // 2 # 쌍 더해주기 ex) 2명 -> 1쌍, 3명 -> 3쌍, 4명 -> 6쌍
    
    # 중복 제거
    weights = list(set(weights))
    
    # 2/3, 2/4, 3/2, 3/4, 4/2, 4/3 중 중복 제거하여
    # 2/3, 2/4, 3/4 만 확인
    for w in weights:
        if w * 2/3 in weights: # 현재 몸무게 * 2/3 인 몸무게가 있다면
            answer += count[w] * count[w * 2/3] # 쌍 구하기 : 현재 몸무게 개수 * 현재 몸무게 *2/3 개수
        if w * 2/4 in weights:
            answer += count[w] * count[w * 2/4]
        if w * 3/4 in weights:
            answer += count[w] * count[w * 3/4]
    
    return answer