n = int(input())
answer = []

for i in range(1, n+1):
    arr = [n, i]
    while arr[-2] - arr[-1] >= 0:
        arr.append(arr[-2] - arr[-1])

    if len(arr) > len(answer):
        answer = arr

print(len(answer))
for a in answer:
    print(a, end=" ")