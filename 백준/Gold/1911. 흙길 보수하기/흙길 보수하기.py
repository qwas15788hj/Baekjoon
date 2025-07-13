n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()
answer = 0
plank = -1
for s, e in arr:
    if plank >= e:
        continue
    s = max(s, plank) # 널판지 시작점

    # 이번에 놓을 널판지 개수
    count = (e-s)//l
    if (e-s)%l != 0:
        count += 1

    answer += count
    plank = (s + (l*count))

print(answer)