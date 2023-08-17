import sys
input = sys.stdin.readline

n = int(input()) # n 입력
dic = dict() # 딕셔너리 생성

for _ in range(n):
    name, check = map(str, input().split()) # 이름, 명령 입력
    if check == "enter": # enter 면
        dic[name] = 1 # 딕셔너리에 추가
    else: # leave 면
        del dic[name] # 딕셔너리에서 삭제

answer = []
# 딕셔너리에 저장된 이름 배열에 저장
for name, check in dic.items():
    answer.append(name)
answer.sort(reverse=True) # 이름 역순으로 정렬

for a in answer:
    print(a)