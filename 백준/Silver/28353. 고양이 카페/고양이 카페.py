n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
s, e = 0, n-1
answer = 0
while True:
    if s >= e:
        break

    if arr[s] + arr[e] <= k:
        answer += 1
        s += 1
        e -= 1
    else:
        e -= 1

print(answer)