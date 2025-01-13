import math, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    add = r1 + r2
    diff = abs(r1 - r2)
    dist = math.sqrt(pow(x1 - x2, 2) + pow(y1- y2, 2))

    answer = 0
    if (dist == 0) and (r1 == r2):
        answer = -1
    elif (add == dist) or (diff == dist):
        answer = 1
    elif diff < dist and dist < add:
        answer = 2

    print(answer)