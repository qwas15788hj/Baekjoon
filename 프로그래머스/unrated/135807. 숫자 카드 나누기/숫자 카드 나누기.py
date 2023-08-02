import math

# 최대공약수 구하는 공식
def gcd(arr):
    num = arr[0]
    for i in range(1, len(arr)):
        num = math.gcd(num, arr[i])
    return num

def solution(arrayA, arrayB):
    answer = 0
    
    a_gcd = gcd(arrayA) # a의 최대공약수
    for i in arrayB: # b 배열 원소 돌면서 체크
        if i % a_gcd == 0: # b 배열 원소 중 하나라도 a의 최대공약수로 나눴을때 나눠지면 실패
            break
    else: # 모두 안나눠지면
        answer = max(answer, a_gcd) # 현재 answer와 a의 최대공약수 비교하여 큰 값으로 변환
        
    b_gcd = gcd(arrayB) # b의 최대공약수
    for i in arrayA: # a 배열 원소 돌면서 체크
        if i % b_gcd == 0: # a 배열 원소 중 하나라도 b의 최대공약수로 나눴을때 나눠지면 실패
            break
    else: # 모두 안나눠지면
        answer = max(answer, b_gcd) # 현재 answer와 b의 최대공약수 비교하여 큰 값으로 변환
    
    return answer