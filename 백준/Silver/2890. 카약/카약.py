r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
team = [0] * 10
check = [0] * (c-5)

for i in range(len(arr)):
    count = 0
    for j in range(c-2, 0, -1):
        if arr[i][j] == ".":
            count += 1
        else:
            team[int(arr[i][j])] = count
            break

    if count < len(check):
        check[count] = 1

for i in range(1, len(team)):
    print(sum(check[:team[i]])+1)