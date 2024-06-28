import sys
input = sys.stdin.readline

n = int(input())
answer = 0
arr = []
for _ in range(n):
    work = list(map(int, input().split()))
    if work[0] == 1:
        if work[2] == 1:
            answer += work[1]
        else:
            arr.append([work[1], work[2]-1])
    else:
        if len(arr) != 0:
            if arr[-1][1] == 1:
                answer += arr[-1][0]
                arr.pop()
            else:
                arr[-1][1] -= 1

print(answer)