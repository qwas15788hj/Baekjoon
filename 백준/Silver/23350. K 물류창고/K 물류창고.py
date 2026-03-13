n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dic = dict()
maxp = 0
for p, w in arr:
    maxp = max(maxp, p)
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

load, rest = [], []
while arr:
    p, w = arr.pop(0)
    # 우선순위 높은 컨테이너 뒤로
    if p < maxp:
        arr.append([p, w])
        answer += w
    # 우선순위 낮거나 같은 컨테이너 적재
    else:
        # 옮겨야 할 컨테이너 우선순위 변경
        dic[p] -= 1
        if dic[p] == 0:
            maxp -= 1

        # 적재 시, 무게가 낮은게 있다면 나머지 공간으로 옮기기
        while load and load[-1][0] <= p and load[-1][1] < w:
            answer += load[-1][1]
            rest.append(load.pop())
        # 현재 컨테이너 적재
        answer += w
        load.append([p, w])

        # 나머지 공간 적재
        while rest:
            answer += rest[-1][1]
            load.append(rest.pop())

print(answer)