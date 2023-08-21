# 하노이 함수
def hanoi(num, start, mid, end, answer):
    if num == 0: # 1
        return
    # 1번 기둥에 있는 n - 1 개를 start -> end -> mid 순으로 옮겨 모두 중앙으로 옮김
    hanoi(num - 1, start, end, mid, answer)
    answer.append([start, end])
    # 2번 기둥에 있는 n - 1 개를 mid -> start -> end 순으로 옮겨 모두 끝으로 옮김
    hanoi(num - 1, mid, start, end, answer)
    

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer