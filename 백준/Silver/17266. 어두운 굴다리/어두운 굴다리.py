n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n+1
answer = 1e9

while start <= end:
    mid = (start+end)//2
    flag = True

    if 0 < arr[0] - mid:
        flag = False
    if arr[-1] + mid < n:
        flag = False

    if flag:
        for i in range(m-1):
            if arr[i+1] - mid > arr[i] + mid:
                flag = False
                break

    if flag:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)