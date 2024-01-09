n = int(input())
arr = [int(input()) for _ in range(n)]

now = sum(arr)//2
for i in range(len(arr)):
    if i%2 != 0:
        now -= arr[i]

answer = [now]
for i in range(len(arr)-1):
    nxt = arr[i] - now
    answer.append(nxt)
    now = nxt

for a in answer:
    print(a)