from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
time = 0

while True:
    # 벨트, 로봇 이동
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 로봇 다음 칸으로 이동 체크
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
        robot[-1] = 0

    # 로봇 올리기
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1

    time += 1

    if belt.count(0) >= k:
        break

print(time)