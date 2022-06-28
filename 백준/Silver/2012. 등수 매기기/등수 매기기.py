import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

answer = 0
for i in range(len(arr)):
    answer += abs((i+1)-arr[i])

print(answer)