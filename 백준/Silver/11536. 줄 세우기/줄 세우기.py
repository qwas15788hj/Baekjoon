n = int(input())
arr = [input() for _ in range(n)]
s_arr = sorted(arr)
r_arr = sorted(arr, reverse=True)
if arr == s_arr:
    print("INCREASING")
elif arr == r_arr:
    print("DECREASING")
else:
    print("NEITHER")