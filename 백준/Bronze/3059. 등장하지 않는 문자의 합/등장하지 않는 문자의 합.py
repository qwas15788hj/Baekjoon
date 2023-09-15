t = int(input())

for _ in range(t):
    s = input()
    arr = [0] * 26 # A ~ Z 배열 생성
    answer = 0
    # 해당 문자가 등장했는지 체크
    for i in s:
        arr[ord(i) - 65] = 1

    # 문자가 등장 안했다면 더해주기
    for i in range(len(arr)):
        if arr[i] == 0:
            answer += i + 65

    print(answer)