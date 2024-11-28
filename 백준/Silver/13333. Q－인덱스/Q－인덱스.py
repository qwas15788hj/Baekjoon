import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

num = [0] * (max(arr)+1)
for i in range(n):
    num[arr[i]] += 1
    
for i in range(len(num)):
    if sum(num[i:]) >= i and sum(num[:i+1]) >= n-i:
        print(i)
        break