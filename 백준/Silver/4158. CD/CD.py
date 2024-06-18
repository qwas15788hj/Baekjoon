import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    dic = dict()
    for _ in range(n):
        dic[int(input())] = 1

    answer = 0
    for _ in range(n):
        if int(input()) in dic:
            answer += 1
    
    print(answer)