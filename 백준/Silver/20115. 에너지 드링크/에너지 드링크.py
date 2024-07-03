n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(n-1):
    answer += arr[i]/2
answer += arr[-1]

if answer == int(answer):
    print(int(answer))
else:
    print(answer)