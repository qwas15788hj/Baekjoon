t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    team = [[] for _ in range(max(arr)+1)]
    check = [False] * (max(arr)+1)
    for i in range(1, max(arr)+1):
        if arr.count(i) == 6:
            check[i] = True

    score = 1
    for i in range(n):
        if check[arr[i]]:
            team[arr[i]].append(score)
            score += 1

    answer = [0, 1e9, 1e9]
    for i in range(1, len(team)):
        if len(team[i]) != 0:
            if answer[1] > sum(team[i][:4]):
                answer = [i, sum(team[i][:4]), team[i][4]]
            elif answer[1] == sum(team[i][:4]):
                if answer[2] > team[i][4]:
                    answer = [i, sum(team[i][:4]), team[i][4]]

    print(answer[0])