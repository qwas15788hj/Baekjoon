n = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in range(n-1, 0, -1):
    if arr[i-1] > arr[i]:
        for j in range(n-1, i-1, -1):
            if arr[i-1] > arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                answer = 1
                break
        break
        
if answer == 1:
    print(*arr)
else:
    print(-1)