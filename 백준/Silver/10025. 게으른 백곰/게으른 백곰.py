n, k = map(int, input().split())
arr = [0] * 1000001
for _ in range(n):
    g, x = map(int, input().split())
    arr[x] = g

nxt = 2*k+1
now = sum(arr[:nxt])
answer = now
for i in range(nxt, 1000001):
    now += arr[i] - arr[i-nxt]
    answer = max(answer, now)

print(answer)