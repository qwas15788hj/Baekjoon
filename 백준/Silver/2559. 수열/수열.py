n, k = map(int, input().split())
arr = list(map(int, input().split()))
sub = [sum(arr[:k])]

# 누적 합 사용
for i in range(k, len(arr)):
    sub.append(sub[-1] + arr[i] - arr[i-k])

print(max(sub))