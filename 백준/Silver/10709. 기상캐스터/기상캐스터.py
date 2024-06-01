h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
answer = [[-1] * w for _ in range(h)]

for i in range(h):
    cloud = -1
    for j in range(w):
        if arr[i][j] == "c":
            answer[i][j] = 0
            cloud = j
        else:
            if cloud != -1:
                answer[i][j] = j-cloud

for a in answer:
    print(*a)