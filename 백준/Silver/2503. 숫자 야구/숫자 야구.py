n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for num in range(100, 1000): # 세 자리 수 돌면서
    now = [str(num)[0], str(num)[1], str(num)[2]]
    # 서로 다른 세 수
    if now[0] == now[1] or now[1] == now[2] or now[0] == now[2]:
        continue
    # 0 제거
    if now[0] == "0" or now[1] == "0" or now[2] == "0":
        continue
    check = 0
    for i in range(n): # 질문 하나씩 체크
        st, ball = 0, 0
        # 현재 질문과 현재 체크 숫자 비교하여
        for j in range(3):
            for z in range(3):
                # 현재 질문 중인 숫자와 현재 체크 중인 숫자가 같다면
                if str(arr[i][0])[j] == now[z]:
                    if j == z: # 자리도 같으면 스트라이크
                        st += 1
                    else: # 자리가 다르면 볼
                        ball += 1

        if st == arr[i][1] and ball == arr[i][2]:
            check += 1
        else:
            break

    if check == n:
        answer += 1

print(answer)