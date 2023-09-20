import sys
input = sys.stdin.readline

# 체스판 생성
arr = []
for _ in range(8):
    s = input()
    sub_arr = []
    for i in range(8):
        sub_arr.append(s[i])
    arr.append(sub_arr)

# 체스판의 가로 + 세로가 짝수면 흰색칸임으로 해당 위치에 F가 있다면 answer 증가
answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and arr[i][j] == "F":
            answer += 1

print(answer)