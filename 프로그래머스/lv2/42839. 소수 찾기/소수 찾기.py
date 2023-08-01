from itertools import permutations # 순열 사용

def solution(numbers):
    answer = 0
    
    arr = [] # 모든 수 담을 배열
    for i in range(1, len(numbers) + 1): # 1개부터 ~ 최대 길이까지
        nums = list(permutations(numbers, i)) # numbers 배열에서 i개만큼 사용해서 순열 생성
        for num in nums: # 만든 순열 배열 요소 돌면서
            num = list(num) # 리스트로 만들고
            num = "".join(num) # 붙여주고
            arr.append(int(num)) # int로 바꾸어 배열에 저장
    
    arr = list(set(arr)) # 중복 제거
    
    for i in arr: # 배열 요소 돌면서
        if i > 1: # 소수구하기
            for j in range(2, int(i**0.5) + 1): # 2 ~ 현재 수인 i의 루트값까지
                if i % j == 0: # 나눠지면 소수 아님
                    break
            else: # 안나눠졌을 경우 소수
                answer += 1
        
    return answer