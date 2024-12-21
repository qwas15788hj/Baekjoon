import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        z = n - (i + j)
        if z >= i + j:
            continue
        else:
            if j > z:
                break
            answer += 1

print(answer)