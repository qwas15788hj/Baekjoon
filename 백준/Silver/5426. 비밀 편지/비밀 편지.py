t = int(input())
for _ in range(t):
    word = input()
    n = int(len(word)**0.5)
    arr = []
    for i in range(n):
        arr.append(word[n*i:n*(i+1)])

    answer = ""
    for i in range(n-1, -1, -1):
        for j in range(n):
            answer += arr[j][i]

    print(answer)