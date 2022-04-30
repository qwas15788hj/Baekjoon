n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.reverse()

answer = 0
score = arr[0]
for i in range(1, n):
    if arr[i] >= score:
        answer += arr[i]-score+1
        score -= 1
    else:
        score = arr[i]
print(answer)