def solution(k, ranges):
    answer = []
    arr = [k] # 콜라츠 작업 진행 저장할 배열
    
    # 콜라츠 작업 진행
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        arr.append(k)
    
    # n 구하기
    n = len(arr) - 1
    
    # 해당 지점 크기 구하기 (사다리꼴 넓이 구하는 공식)
    size = []
    for i in range(1, len(arr)):
        size.append((arr[i] + arr[i-1])/2)
        
    # 넓이 구하기
    for s, e in ranges:
        if e <= 0: # 끝 지점이 0이하면 끝지점 재생성
            e = n + e
        
        if s > e: # 시작점이 끝지점보다 크면 -1 저장
            answer.append(-1)
        else: # 끝지점이 시작점보다 크면
            count = 0
            for i in range(s, e): # 시작 지점 ~ 끝 지점 넓이 구하기
                count += size[i]
            answer.append(count)
    
    return answer