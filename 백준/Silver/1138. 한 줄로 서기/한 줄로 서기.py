n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if count == arr[i] and answer[j] == 0:
            answer[j] = i+1
            break
        if answer[j] == 0:
            count += 1

for a in answer:
    print(a, end=" ")