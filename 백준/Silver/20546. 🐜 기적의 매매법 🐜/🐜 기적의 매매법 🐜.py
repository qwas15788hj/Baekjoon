import sys
input = sys.stdin.readline

money = int(input())
arr = list(map(int, input().split()))

jun_m, jun_s = money, 0
for i in range(len(arr)-1):
    if jun_m >= arr[i]:
        jun_s += jun_m // arr[i]
        jun_m = jun_m % arr[i]

sung_m, sung_s = money, 0
for i in range(3, len(arr)-1):
    if (arr[i-3] > arr[i-2]) and (arr[i-2] > arr[i-1]) and (arr[i-1] > arr[i]):
        sung_s += sung_m // arr[i]
        sung_m = sung_m % arr[i]
    if (arr[i-3] < arr[i-2]) and (arr[i-2] < arr[i-1]) and (arr[i-1] < arr[i]):
        sung_m += sung_s * arr[i]
        sung_s = 0

jun_m += jun_s * arr[-1]
sung_m += sung_s * arr[-1]
if jun_m > sung_m:
    print("BNP")
elif jun_m < sung_m:
    print("TIMING")
else:
    print("SAMESAME")