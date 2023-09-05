import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n, m 입력
arr = [[] for _ in range(n)] # 팀 수 n만큼 멤버 이름 저장할 배열 생성
dic = dict() # 팀의 인덱스 번호를 저장할 딕셔너리 생성

# 딕셔너리와 배열에 팀 이름 맞춰서 넣기
for i in range(n):
    team = input() # 팀 입력
    dic[team] = i # 팀의 인덱스 설정
    k = int(input())
    for _ in range(k):
        arr[i].append(input()) # 해당 인덱스에 멤버 이름 넣기
    arr[i].sort() # 이름 순으로 정렬

# 이름 혹은 팀 이름 출력 과정
for _ in range(m):
    s = input()
    p = int(input())
    if p == 0: # p가 0이면
        for member in arr[dic[s]]: # s가 팀 이름임으로 해당 팀의 인덱스에 맞는 배열에서 멤버이름 출력
            print(member, end = "")
    else: # p가 1이면
        # 해당 이름이 몇번째 배열에 있는지 인덱스 찾기
        check = 0
        for i in range(n):
            if s in arr[i]:
                check = i
                break
        # 딕서너리 돌면서 찾은 인덱스와 같은 번호인 팀 이름 출력
        for v, w in dic.items():
            if w == check:
                print(v, end = "")
                break