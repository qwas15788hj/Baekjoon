from itertools import product

n, k = map(int, input().split())
arr = list(map(int, input().split()))
rang = [list(map(int, input().split())) for _ in range(k)]
merry = [list(map(int, input().split())) for _ in range(k)]

answer = 0
pro = list(product(range(n), repeat=k))
for r in pro: # 랑 캔
    for m in pro: # 메리 캔
        check = [0] * n # 캔 개수 확인
        flag = True
        for i in range(k):
            check[r[i]] += 1
            check[m[i]] += 1
        for i in range(n):
            if check[i] > arr[i]:
                flag = False
                break

        # 캔 개수가 부족하지 않다면 진행
        if flag:
            score = 0
            for i in range(k):
                score += rang[i][r[i]]
                score += merry[i][m[i]]

            answer = max(answer, score)

print(answer)