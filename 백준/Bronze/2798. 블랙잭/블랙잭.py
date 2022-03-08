n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_score = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for r in range(j+1, n):
            if arr[i] + arr[j] + arr[r] > m:
                continue
            else:
                max_score = max(max_score, arr[i]+arr[j]+arr[r])
print(max_score)