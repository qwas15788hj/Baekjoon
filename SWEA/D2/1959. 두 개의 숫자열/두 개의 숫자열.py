t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = 0
    
    if len(a) > len(b):
        a, b = b, a
    
    for i in range(len(b)-len(a)+1):
        count = 0
        for j in range(len(a)):
            count += a[j]*b[j+i]
        if count > answer:
            answer = count
    
    print("#{} {}" .format(tc, answer))