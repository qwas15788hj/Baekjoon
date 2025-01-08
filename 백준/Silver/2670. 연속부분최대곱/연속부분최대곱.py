import sys
input = sys.stdin.readline

n = int(input())
arr = [float(input()) for _ in range(n)]

answer, num = arr[0], 1
for i in range(n):
    if arr[i] >= num * arr[i]:
        num = arr[i]
    else:
        num *= arr[i]
    answer = max(answer, num)

print("%.3f"%answer)