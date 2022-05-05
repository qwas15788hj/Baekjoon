def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0

n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
array.sort()

for i in x:
    answer = binary_search(array, i, 0, n-1)
    print(answer)