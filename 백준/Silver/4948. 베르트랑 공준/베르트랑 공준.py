arr = [True] * 250000
arr[0] = False
arr[1] = False
for i in range(2, 250000):
    if arr[i] == True:
        j = 2
        while (i * j) < 250000:
            arr[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    answer = 0
    for i in range(n+1, 2*n+1):
        if arr[i]:
            answer += 1

    print(answer)