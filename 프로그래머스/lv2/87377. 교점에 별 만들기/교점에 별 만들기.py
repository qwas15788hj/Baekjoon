from itertools import combinations

def calcu(eq1, eq2):
    a, b, e = eq1
    c, d, f = eq2
    
    # 기울기가 같으면 교점 없음
    if a*d - b*c == 0:
        return
    
    # 교점 찾기
    x = (b*f - e*d) / (a*d - b*c)
    y = (e*c - a*f) / (a*d - b*c)
    
    if x == int(x) and y == int(y):
        return [int(x), int(y)]

def solution(line):
    points = [] # 교점들 저장할 배열
    
    # 모든 선분의 조합을 통해 교점 찾기
    for eq1, eq2 in combinations(line, 2):
        point = calcu(eq1, eq2)
        if point:
            points.append(point)
    
    # 교점 중 x 축 최소, 최대 찾기
    points.sort(key = lambda x:x[0])
    w1 = points[0][0] # 최소
    w2 = points[-1][0] + 1 # 최대
    
    # 교점 중 y 축 최소, 최대 찾기
    points.sort(key = lambda x:x[1])
    h1 = points[0][1] # 최소
    h2 = points[-1][1] + 1 # 최대
    
    answer = [["."] * (w2 - w1) for _ in range(h1, h2)] # x, y 각각 최소, 최대 값에 맞게 . 생성
    
    # 교점 별로 * 체크
    for x, y in points:
        answer[y - h1][x - w1] = "*"
    # 거꾸로
    answer.reverse()
    
    return ["".join(a) for a in answer] # 리스트 하나로 합쳐서 return