def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)] # 1 ~ n까지 원소를 갖는 배열 생성
    count = 1 # 현재 위치에 하나의 번호가 몇가지 경우의 수를 갖는지
    now = n # count 나눠줄 값
    for i in range(2, n): # 2 ~ n-1까지 count에 곱하여 맨 앞에 자리 수 경우의 수 구하기
        count *= i
    
    while len(answer) < n-1: # 마지막 한자리 남겨놓고 다 정할 때까지
        idx = (k-1)//count # 현재 위치에 올 값에 대한 인덱스 값
        answer.append(arr.pop(idx)) # 배열에서 해당 인덱스 뽑아서 answer에 넣기
        k %= count # 다음 자리 수의 경우의 수 구하기
        now -= 1 # 나눠줄 값 - 1 이후
        count //= now # count에서 나눠주기
    
    answer.append(arr.pop()) # 마지막 한자리 수 배열에서 뽑기
    
    return answer