import sys
input = sys.stdin.readline

n = int(input()) # n 입력
cnt = 0
num = 0 # 자리 수
while cnt < n:
    num += 1
    cnt += 9 * (10**(num-1)) * num

cnt -= 9 * (10**(num-1)) * num
a = (n - cnt) // num
b = (n - cnt) % num

if b == 0:
    print(str(10**(num-1) + (a-1))[-1])
else:
    print(str(10**(num-1) + a)[b-1])