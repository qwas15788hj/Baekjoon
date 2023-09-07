import sys
input = sys.stdin.readline

n = int(input()) # n 입력
files = list(map(int, input().split())) # 파일 목록 입력
cluster = int(input()) # 클러스터 입력

answer = 0 # 총 필요한 클러스터 양
for file in files: # 파일 목록 돌면서
    if file == 0: # 파일 크기가 0이면
        disk = 0 # 0개 사용
    elif 0 < file <= cluster: # 파일 크기가 0 보다 크고 클러스터 이하면
        disk = 1 # 1개 사용
    else: # 파일 크기가 클러스터 보다 크면
        disk = file // cluster # 해당 몫만큼 사용
        if file % cluster != 0: # 나머지 용량이 있다면
            disk += 1 # 하나 더 추가

    answer += disk * cluster

print(answer)