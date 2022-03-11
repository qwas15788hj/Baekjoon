n, m = map(int, input().split())
arr = []
answer = 0

for _ in range(m):
    price = list(map(int, input().split()))
    arr.append(price)
    
six_list = sorted(arr, key=lambda x:x[0])
one_list = sorted(arr, key=lambda x:x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    answer = six_list[0][0]*(n//6) + one_list[0][1]*(n%6)
    if six_list[0][0] < one_list[0][1] * (n%6):
        answer = six_list[0][0]*(n//6+1)
else:
    answer = one_list[0][1]*n
print(answer)