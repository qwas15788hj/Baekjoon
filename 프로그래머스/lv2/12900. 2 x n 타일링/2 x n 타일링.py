def solution(n):
    arr = [0] * 60001 # 60001개 배열 생성
    arr[1] = 1 # 가로 1일때, 1가지
    arr[2] = 2 # 가로 2일때, 2가지
    for i in range(3, n+1): # 가로 길이 3 ~ n까지
        arr[i] = (arr[i-2] + arr[i-1]) % 1000000007 # 현재 가로 = (현재 가로 - 2) + (현재 가로 - 1)
    
    return arr[n] % 1000000007 # 가로 길이가 n인 n번째 배열 return