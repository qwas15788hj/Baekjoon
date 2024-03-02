n = int(input())
arr = [0] + list(map(int, input().split()))
score = [0] * (n+1)

for i in range(1, n+1):
    if arr[i] == 1:
        score[i] = max(1, score[i-1]+1)

print(sum(score))