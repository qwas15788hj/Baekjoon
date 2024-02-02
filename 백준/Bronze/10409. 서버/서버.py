n, t = map(int, input().split())
arr = list(map(int, input().split()))
time = 0
answer = 0
for i in range(n):
    time += arr[i]
    if time > t:
        break
    else:
        answer += 1

print(answer)