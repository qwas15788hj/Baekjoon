import sys
input = sys.stdin.readline

n = int(input()) # n 입력
answer = 0 # 총 걸린 시간
sing = 1 # 현재 부를 노래
while n != 0: # n이 0이 될때까지
    if sing > n: # 현재 노래가 남은 새 n보다 크면
        sing = 1 # 노래 1로 갱신

    n -= sing # 노래 만큼 새 빼기
    sing += 1 # 노래 증가
    answer += 1 # 시간 증가

print(answer)