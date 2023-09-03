import sys
input = sys.stdin.readline

group = 0
while True: # 무한 반복
    n = int(input()) # n 입력
    # n이 0이면 종료
    if n == 0:
        break

    if group != 0:
        print()
    # 그룹 증가 후 출력
    group += 1
    print("Group", group)

    # 활동 저장
    arr = []
    for _ in range(n):
        arr.append(list(map(str, input().split())))

    # 이름 저장 (두 번째 부터 저장)
    name = []
    for i in range(1, len(arr)):
        name.append(arr[i][0])

    # 나쁜 말 존재하는지 체크
    flag = True
    nasty = []
    for i in arr:
        if "N" in i:
            flag = False

    # 나쁜 말 없다면
    if flag:
        print("Nobody was nasty")
    # 나쁜 말 있다면
    else:
        # 배열 돌면서 N 이 누가 누구에게 출력
        for i in range(len(arr)):
            now = arr[i]
            for j in range(len(now)):
                if now[j] == "N":
                    nasty.append([name[-j], arr[i][0]])

            # 이름 배열 재생성
            name = name[1:]
            name.append(arr[i][0])

        for n in nasty:
            print(n[0], "was nasty about", n[1])