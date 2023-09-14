import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n, m 입력
arr = list(map(int, input().split())) # 일급 입력
add_arr = [sum(arr[:m])] # 누적합 위해 새로운 배열 생성 후 m-1 일까지 일급 더한 값 저장

for i in range(m, n): # m ~ n 까지
    # 현재 누적으로 받은 값 + 오늘 받을 일급 - 가장 처음 받은 일급
    add_arr.append(add_arr[-1] + arr[i] - arr[i-m])

print(max(add_arr)) # 누적합 배열에서 가장 큰 값 출력