import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def binary_Search(target, array, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in m_list:
    result = binary_Search(i, n_list, 0, n-1)
    if result == None:
        print(0, end=' ')
    else:
        print(1, end=' ')