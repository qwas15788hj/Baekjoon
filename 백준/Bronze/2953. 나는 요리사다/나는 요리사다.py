idx, score = 0, 0
for i in range(5):
    arr = list(map(int, input().split()))
    if sum(arr) > score:
        idx = i+1
        score = sum(arr)

print(idx, score)