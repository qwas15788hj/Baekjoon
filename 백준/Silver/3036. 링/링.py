import math

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    a = math.gcd(arr[0], arr[i])
    print(f'{arr[0]//a}/{arr[i]//a}')