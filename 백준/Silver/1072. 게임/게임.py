import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y*100)//x

answer = 0
start = 1
end = x

while start <= end:
    mid = (start+end)//2
    if (y+mid)*100//(x+mid) == z:
        start = mid+1
    else:
        end = mid-1
        answer = mid

if answer == 0:
    answer = -1
print(answer)