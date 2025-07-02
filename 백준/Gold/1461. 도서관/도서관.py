import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 왼쪽(음수) / 오른쪽(양수) 분리
left, right = [], []
for x in arr:
    if x > 0:
        right.append(x)
    else:
        left.append(abs(x)) # 절댓값으로 저장

# 내림차순 정렬 (가장 먼 책부터)
left.sort(reverse=True)
right.sort(reverse=True)

# 모든 책을 가져다 놓고, 0으로 돌아오는 거리
answer, idx = 0, 0
# 왼쪽 처리
while m*idx < len(left):
    answer += left[m*idx]*2 # 왕복 거리
    idx += 1

# 오른쪽 처리
idx = 0
while m*idx < len(right):
    answer += right[m*idx]*2 # 왕복 거리
    idx += 1

# 가장 먼 거리 한 번은 편도로 처리
# 왼쪽 / 오른쪽이 모두 존재할 수 있으므로 예외 처리
if len(left) == 0:
    answer -= right[0]
elif len(right) == 0:
    answer -= left[0]
else:
    answer -= max(left[0], right[0])

print(answer)