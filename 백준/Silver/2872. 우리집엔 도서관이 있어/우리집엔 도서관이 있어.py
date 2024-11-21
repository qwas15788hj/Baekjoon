import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

target = n
answer = 0
for i in range(n-1, -1, -1):
    if arr[i] != target:
        answer += 1
    else:
        target -= 1

print(answer)