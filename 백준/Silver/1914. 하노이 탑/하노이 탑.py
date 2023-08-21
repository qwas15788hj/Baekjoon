import sys
input = sys.stdin.readline

n = int(input()) # n 입력

# 하노이 탑 수행 함수
def hanoi(num, start, mid, end, answer):
    if num == 0: # 개수가 0이면 종료
        return

    # 1번 시작점에 있는 n - 1개 원판 start -> end -> mid 순으로 옮겨 2번으로 모두 옮기기
    hanoi(num - 1, start, end, mid, answer)
    answer.append([start, end]) # 시작점, 끝점 추가
    # 2번 시작점에 있는 n - 1개 원판 mid -> start -> end 순으로 옮겨 3번으로 모두 옮기기
    hanoi(num - 1, mid, start, end, answer)

print(2**n - 1) # 이동 횟수 = 2^n - 1번
if n <= 20: # n이 20 이하일 경우만 과정 출력
    answer = []
    hanoi(n, 1, 2, 3, answer) # 하노이 함수 호출
    for s, e in answer:
        print(s, e)