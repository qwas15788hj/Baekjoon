n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n%2 == 0:
    answer = arr[0] + arr[-1]
    for i in range(n//2):
        answer = max(answer, arr[i] + arr[-(i+1)])
else:
    answer = arr[-1]
    for i in range(n//2):
        answer = max(answer, arr[i] + arr[-(i+2)])

print(answer)