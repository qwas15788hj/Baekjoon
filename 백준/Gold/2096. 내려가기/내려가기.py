import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최대값 계산
prev1, prev2, prev3 = arr[0][0], arr[0][1], arr[0][2]
nxt1, nxt2, nxt3 = 0, 0, 0
for i in range(1, n):
    nxt1 = arr[i][0] + max(prev1, prev2)
    nxt2 = arr[i][1] + max(max(prev1, prev2), prev3)
    nxt3 = arr[i][2] + max(prev2, prev3)
    prev1, prev2, prev3 = nxt1, nxt2, nxt3

max_val = max(max(prev1, prev2), prev3)

# 최소값 계산 (같은 방식으로 진행)
prev1, prev2, prev3 = arr[0][0], arr[0][1], arr[0][2]
nxt1, nxt2, nxt3 = 0, 0, 0
for i in range(1, n):
    nxt1 = arr[i][0] + min(prev1, prev2)
    nxt2 = arr[i][1] + min(min(prev1, prev2), prev3)
    nxt3 = arr[i][2] + min(prev2, prev3)
    prev1, prev2, prev3 = nxt1, nxt2, nxt3

min_val = min(min(prev1, prev2), prev3)

print(max_val, min_val)