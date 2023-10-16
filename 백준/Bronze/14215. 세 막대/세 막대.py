arr = list(map(int, input().split()))
arr.sort()
# 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야한다
print(arr[0] + arr[1] + min(arr[0] + arr[1]-1, arr[2]))