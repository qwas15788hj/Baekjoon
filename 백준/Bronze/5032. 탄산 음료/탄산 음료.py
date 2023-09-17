import sys
input = sys.stdin.readline

e, f, c = map(int, input().split()) # e, f, c 입력
e += f # 처음 가지고 있는 총 병수
answer = 0 # 마신 수
while e >= c: # 총 병수가 필요한 병수보다 크거나 같으면 계속
    change = e//c # 바꿀 수 있는 병 수
    answer += change # 바꿔서 마시기
    e = e - change * c + change # 처음 병 - 바꾼 병 수 + 받은 병 수

print(answer)