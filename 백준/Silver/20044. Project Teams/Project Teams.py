import sys
input = sys.stdin.readline

n = int(input()) # n 입력
arr = list(map(int, input().split())) # 학생들의 코딩 능력 입력
arr.sort() # 정렬

answer = 1e9 # 최종 출력 값, 초기 최대값으로
for i in range(n): # n 개의 팀 생성임으로 n 반복
    # 가장 코딩 능력이 낮은 학생과 높은 학생이 팀을 이루고, answer 와 작은 값으로 갱신
    answer = min(answer, arr[i] + arr[-(i+1)])

print(answer)