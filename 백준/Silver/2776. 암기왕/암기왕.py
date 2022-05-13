t = int(input())

def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    arr1.sort()
    for i in range(m):
        if binary_search(0, n-1, arr1, arr2[i]) == None:
            print(0)
        else:
            print(1)