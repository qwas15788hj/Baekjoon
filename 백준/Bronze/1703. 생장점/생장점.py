import sys
input = sys.stdin.readline

# 무한 반복
while True:
    arr = list(map(int, input().split())) # 나무 입력
    # 0 등장시 종료
    if arr[0] == 0:
        break

    # 잎 개수 구하기
    leaf = 1 # 초기 1
    for i in range(1, len(arr), 2): # 1 ~ 배열까지, 2씩 증가하며
        leaf = leaf * arr[i] - arr[i+1] # 나뭇잎 = 나뭇잎 * 뻗는 개수 - 가지치기

    print(leaf)