import heapq, sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 가운데 값을 기준으로, left / right 분류
left, right = [], []
center = arr[0]
for i in range(n):
    if i != 0:
        # center 보다 값이 작으면 -> left (이후 pop을 위해 '-'를 추가로 붙여서 저장)
        # center 보다 값이 크면 -> right
        if center > arr[i]:
            heapq.heappush(left, -arr[i])
        else:
            heapq.heappush(right, arr[i])

        # left > right -> left의 가장 큰 값 center
        # right > left+1 -> right의 가장 작은 값 center
        if len(left) > len(right):
            heapq.heappush(right, center)
            center = -heapq.heappop(left)
        elif len(right) > len(left) + 1:
            heapq.heappush(left, -center)
            center = heapq.heappop(right)

    print(center)