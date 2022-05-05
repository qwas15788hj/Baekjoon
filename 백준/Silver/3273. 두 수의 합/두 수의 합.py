import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
answer = 0
i, j = 0, n-1

while i != j:
    if arr[i]+arr[j] == x:
        answer += 1
        i += 1
    elif arr[i]+arr[j] > x:
        j -= 1
    else:
        i += 1
print(answer)