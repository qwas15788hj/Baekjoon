n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = sum(arr[-k:])
for i in range(1, k):
    answer -= i

print(answer)