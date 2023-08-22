import sys
input = sys.stdin.readline

n = int(input())
start = 0
end = n

while start <= end:
    mid = (start + end)//2
    if mid**2 == n:
        print(mid)
        break
    if mid**2 > n:
        end = mid - 1
    else:
        start = mid + 1