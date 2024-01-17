m, n = map(int, input().split())
t = int(input())
arr = []
for _ in range(t+1):
    a, b = map(int, input().split())
    if a == 1:
        arr.append([0, b])
    elif a == 2:
        arr.append([n, b])
    elif a == 3:
        arr.append([b, 0])
    elif a == 4:
        arr.append([b, m])

answer = 0
for i in range(t):
    # 동근이가 북쪽일 때
    if arr[-1][0] == 0:
        # 상점이 북쪽일 때
        if arr[i][0] == 0:
            answer += abs(arr[i][1] - arr[-1][1])
        # 상점이 남쪽일 때
        elif arr[i][0] == n:
            left = arr[-1][1] + n + arr[i][1]
            right = (m - arr[-1][1]) + n + (m - arr[i][1])
            answer += min(left, right)
        # 상점이 서쪽일 때
        elif arr[i][1] == 0:
            answer += arr[-1][1] + arr[i][0]
        # 상점이 동쪽일 때
        elif arr[i][1] == m:
            answer += (m - arr[-1][1]) + arr[i][0]

    # 동근이가 남쪽일 때
    elif arr[-1][0] == n:
        # 상점이 북쪽일 때
        if arr[i][0] == 0:
            left = arr[-1][1] + n + arr[i][1]
            right = (m - arr[-1][1]) + n + (m - arr[i][1])
            answer += min(left, right)
        # 상점이 남쪽일 때
        elif arr[i][0] == n:
            answer += abs(arr[i][1] - arr[-1][1])
        # 상점이 서쪽일 때
        elif arr[i][1] == 0:
            answer += arr[-1][1] + (n - arr[i][0])
        # 상점이 동쪽일 때
        elif arr[i][1] == m:
            answer += (m - arr[-1][1]) + (n - arr[i][0])

    # 동근이가 서쪽일 떄
    elif arr[-1][1] == 0:
        # 상점이 북쪽일 때
        if arr[i][0] == 0:
            answer += arr[-1][0] + arr[i][1]
        # 상점이 남쪽일 때
        elif arr[i][0] == n:
            answer += (n - arr[-1][0]) + arr[i][1]
        # 상점이 서쪽일 때
        elif arr[i][1] == 0:
            answer += abs(arr[i][0] - arr[-1][0])
        # 상점이 동쪽일 때
        elif arr[i][1] == m:
            left = arr[-1][0] + m + arr[i][0]
            right = (n - arr[-1][0]) + m + (n - arr[i][0])
            answer += min(left, right)

    # 동근이가 동쪽일 때
    elif arr[-1][1] == m:
        # 상점이 북쪽일 때
        if arr[i][0] == 0:
            answer += arr[-1][0] + (m - arr[i][1])
        # 상점이 남쪽일 때
        elif arr[i][0] == n:
            answer += (n - arr[-1][0]) + (m - arr[i][1])
        # 상점이 서쪽일 때
        elif arr[i][1] == 0:
            left = (n - arr[-1][0]) + m + (n - arr[i][0])
            right = arr[-1][0] + m + arr[i][0]
            answer += min(left, right)
        # 상점이 동쪽일 때
        elif arr[i][1] == m:
            answer += abs(arr[i][0] - arr[-1][0])

print(answer)