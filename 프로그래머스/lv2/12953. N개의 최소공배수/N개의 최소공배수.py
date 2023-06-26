import math

def solution(arr):

    result = arr[0] # 첫 수
    for i in range(1, len(arr)):
        # 최소공배수 = 현재 수 * 다음 수 // 현재 수와 다음 수의 최대공약수
        result = arr[i] * result // math.gcd(arr[i], result)
    
    return result