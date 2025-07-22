n = int(input())
dice = list(map(int, input().split()))

arr = []
for i in range(3):
    arr.append(min(dice[i], dice[-(i+1)]))
arr.sort()

if n == 1:
    print(sum(dice)-max(dice))
else:
    dic = dict()
    count = [0] * 4

    # 바닥 ~ 꼭대기 전
    for _ in range(n-1):
        count[1] += (n-2) * 4
        count[2] += 4
        
    # 꼭대기
    count[3] += 4
    count[2] += (n-2) * 4
    count[1] += (n**2 - ((n-2)*4 + 4))

    answer = 0
    for i in range(1, 4):
        answer += count[i] * sum(arr[:i])

    print(answer)