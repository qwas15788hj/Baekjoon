import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    result = -1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            result = mid
            start = mid+1
        else:
            end = mid-1
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    m_arr.sort()
  
    count = 0
    for i in n_arr:
        count += binary_search(m_arr, i) + 1
        
    print(count)