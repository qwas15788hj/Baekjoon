n, c = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]

arr.sort(key=lambda x:(x[1], x[0]))
weight = [0] * (n+1)
answer = 0
for s, e, w in arr:
    # 담을 수 있는 가능한 무게
    possible = min(c - max(weight[s:e]), w)

    for i in range(s, e):
        weight[i] += possible
    answer += possible

print(answer)