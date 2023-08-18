import math
    
def solution(w,h):
    
    num = math.gcd(w, h) # 가로, 세로의 최대공약수
    x = w // num # 최대공약수로 나눈 가로 값
    y = h // num # 최대공약수로 나눈 세로 값
    
    # 가로 x, 세로 y값을 갖는 직사각형에서 영향을 받는 사각형은 x + y - 1개
    # 모든 개수 - (반복 횟수 * 영향 받는 사각형개수)
    return (w * h) - (num * (x + y - 1))