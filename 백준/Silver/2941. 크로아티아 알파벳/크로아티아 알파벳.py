s = input()
arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count_arr = [0, 0, 0, 0, 0, 0, 0, 0]
answer = 0
count = 0
for i in range(len(arr)):
    count_arr[i] += s.count(arr[i])
count_arr[-1] = max(count_arr[-1] - count_arr[2], 0)

for i in range(len(arr)):
    answer += count_arr[i]
    count += count_arr[i] * len(arr[i])

print(answer + len(s) - count)