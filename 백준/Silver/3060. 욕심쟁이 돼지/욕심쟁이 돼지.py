t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 1
    nxt_arr = [0] * 6
    while True:
        if sum(arr) > n:
            break
        for i in range(6):
            nxt_arr[i] = arr[i] + arr[i-1] + arr[(i+1)%6] + arr[(i+3)%6]
        arr = nxt_arr[:]
        
        answer += 1
        
    print(answer)