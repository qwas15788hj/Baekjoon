n = int(input())
left, right, zero = [], [], 0
answer = 0
for _ in range(n):
    m = int(input())
    if m < 0:
        left.append(m)
    elif m == 0:
        zero += 1
    # 1일 때는, 양수에 넣지 않고 answer에 직접 더함
    elif m == 1:
        answer += 1
    else:
        right.append(m)

left.sort()
right.sort(reverse=True)

# 음수 최대값 만들기
for i in range(0, len(left)//2):
    answer += (left[i*2] * left[i*2+1])
# 음수가 홀수 일 때, 0이 없으면 빼야함
if (len(left)%2 != 0) and zero == 0:
    answer += left[-1]

# 양수 최대값 만들기
for i in range(0, len(right)//2):
    answer += (right[i*2] * right[i*2+1])
if (len(right)%2 != 0):
    answer += right[-1]

print(answer)