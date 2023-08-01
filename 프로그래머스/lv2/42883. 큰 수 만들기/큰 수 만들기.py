def solution(number, k):
    arr = [] # 숫자 담을 배열
    count = 0 # 뺀 개수
    
    arr.append(number[0]) # 배열에 맨 처음 값 넣기
    for i in range(1, len(number)): # 배열 1부터 끝까지 돌면서
        if len(arr) == 0: # 배열에 담긴게 없으면
            arr.append(number[i]) # 현재 숫자 넣고
        else: # 배열에 담긴게 있다면
            # 배열에 요소가 있고, 배열 끝과 현재 숫자를 비교하고, 뺄 수 있다면
            while arr and arr[-1] < number[i] and count < k:
                arr.pop() # 맨 끝 빼고
                count += 1 # 뺀 수 증가
            arr.append(number[i]) # 마지막에는 현재 숫자 넣기
    
    for i in range(k - count): # 뺄 수가 남았다면 남은 만큼
        arr.pop() # 배열에서 빼주기

    return "".join(arr)