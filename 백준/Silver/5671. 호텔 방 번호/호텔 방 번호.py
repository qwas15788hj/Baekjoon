import sys
input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
        answer = 0
        for i in range(n, m+1):
            if len(set(str(i))) == len(str(i)):
                answer += 1
        print(answer)

    except:
        break