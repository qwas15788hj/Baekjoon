import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
answer = -1
for i in range(n-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        answer = arr[i] + arr[i+1] + arr[i+2]
        break

print(answer)