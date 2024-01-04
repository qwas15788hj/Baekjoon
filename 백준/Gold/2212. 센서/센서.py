n = int(input())
k = int(input())
arr = list(map(int, input().split()))

dist = []
arr.sort()
for i in range(n-1):
    dist.append(arr[i+1] - arr[i])

dist.sort()
answer = 0
for i in range(len(dist) - (k-1)):
    answer += dist[i]

print(answer)