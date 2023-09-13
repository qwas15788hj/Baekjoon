import sys
input = sys.stdin.readline

m = int(input()) # m 입력
answer = 1 # 공이 있는 번호, 최초 1번
for _ in range(m): # m 만큼 반복
    x, y = map(int, input().split()) # x, y 입력
    if x == answer: # x 가 공 위치라면
        answer = y # y 로 이동
        continue # 이후 무시
    if y == answer: # y 가 공 위치라면
        answer = x # x 로 이동

print(answer)