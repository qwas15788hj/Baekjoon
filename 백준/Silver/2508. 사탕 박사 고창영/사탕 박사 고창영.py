t = int(input())
for _ in range(t):
    block = input()
    r, c = map(int, input().split())
    arr = [list(input()) for _ in range(r)]

    answer = 0
    for i in range(r):
        for j in range(c):
            if 0 < j < c-1:
                if arr[i][j] == 'o' and arr[i][j-1] == '>' and arr[i][j+1] == '<':
                    answer += 1
            if 0 < i < r-1:
                if arr[i][j] == 'o' and arr[i-1][j] == 'v' and arr[i+1][j] == '^':
                    answer += 1

    print(answer)