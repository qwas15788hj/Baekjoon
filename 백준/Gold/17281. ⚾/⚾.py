import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
# 몇 번째 선수가 몇 번째 타자로 설 것인지
num_list = [1, 2, 3, 4, 5, 6 ,7 ,8]
for num in list(permutations(num_list, 8)):
    now = [[0] * 9 for _ in range(n)] # 이번 경우의 모든 이닝을 저장하는 배열
    for i in range(len(arr)):
        now[i][3] = arr[i][0]
        for j in range(len(num)):
            if j < 3:
                now[i][j] = arr[i][num[j]]
            else:
                now[i][j+1] = arr[i][num[j]]

    # now를 통해서 점수 계산
    idx = 0
    score = 0
    for i in range(len(now)):
        field = [0, 0, 0, 0]
        out = 0
        # 한 이닝 진행
        while True:
            if out == 3:
                break

            # 안타
            if now[i][idx] == 1:
                score += field[3]
                field[3] = field[2]
                field[2] = field[1]
                field[1] = 1
            # 2루타
            elif now[i][idx] == 2:
                score += (field[3] + field[2])
                field[3] = field[1]
                field[2] = 1
                field[1] = 0
            # 3루타
            elif now[i][idx] == 3:
                score += (field[3] + field[2] + field[1])
                field[3] = 1
                field[2] = 0
                field[1] = 0
            # 홈런
            elif now[i][idx] == 4:
                score += (field[3] + field[2] + field[1] + 1)
                field[3] = 0
                field[2] = 0
                field[1] = 0
            # 아웃
            elif now[i][idx] == 0:
                out += 1

            idx = (idx+1)%9

    answer = max(answer, score)

print(answer)