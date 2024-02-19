n = int(input())
arr = list(map(int, input().split()))
answer = []

for i in range(n):
    answer.insert(arr[i], i+1)

for i in range(n-1, -1, -1):
    print(answer[i], end=" ")