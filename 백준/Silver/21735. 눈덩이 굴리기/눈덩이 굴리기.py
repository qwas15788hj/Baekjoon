from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))
step = [1, 2]

answer = 0
for now in list(product(step, repeat=m)):
    size = 1
    idx = -1
    for i in now:
        idx += i
        if idx < n:
            if i == 1:
                size += arr[idx]
            else:
                size = size//2 + arr[idx]
        else:
            break
            
    answer = max(answer, size)

print(answer)