p = int(input())
for _ in range(p):
    sub_arr = list(map(int, input().split()))
    n = sub_arr[0]
    arr = sub_arr[1:]
    answer = 0
    # 2번째 ~ 끝까지
    for i in range(1, len(arr)):
        # 현재 체크할 번호
        now = arr[i]
        # 처음 ~ i 번 전까지
        for j in range(i):
            # 앞 사람이 현재 체크할 사람보다 크면
            if arr[j] > arr[i]:
                arr.insert(j, arr.pop(i))
                answer += abs(i - j)
                break

    print(n, answer)