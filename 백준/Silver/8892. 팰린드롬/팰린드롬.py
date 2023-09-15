t = int(input()) # t 입력
for _ in range(t): # t 번 진행
    k = int(input()) # 단어 개수 입력
    arr = [] # 단어 저장할 배열
    for _ in range(k): # 단어 저장
        arr.append(input())

    flag = False # 찾았는지 체크
    word = "" # 현재 체크할 단어
    # 배열 돌면서 팰린드롬 찾기
    for i in range(k):
        for j in range(k):
            if i == j: # 같은 단어면 무시
                continue
            word = arr[i] + arr[j] # 두 단어 합치기
            if word == word[::-1]: # 현재 단어가 반대로해도 같으면 찾음
                flag = True
                break
        if flag:
            break

    if flag:
        print(word)
    else:
        print(0)