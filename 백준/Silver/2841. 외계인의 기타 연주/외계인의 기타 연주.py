import sys
input = sys.stdin.readline

n, p = map(int, input().split())
arr = [[] for _ in range(7)]
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    if len(arr[a]) == 0:
        arr[a].append(b)
        answer += 1
    else:
        while True:
            if len(arr[a]) == 0:
                break
            if arr[a][-1] <= b:
                break
            arr[a].pop()
            answer += 1

        if len(arr[a]) == 0 or arr[a][-1] < b:
            arr[a].append(b)
            answer += 1

print(answer)