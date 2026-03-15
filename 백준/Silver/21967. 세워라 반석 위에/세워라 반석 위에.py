n = int(input())
arr = list(map(int, input().split()))

count = [0] * 11
left, answer = 0, 0
for right in range(n):
    count[arr[right]] += 1
    while True:
        min_v = 0
        max_v = 0
        for i in range(1, 11):
            if count[i] > 0:
                max_v = i
                if min_v == 0:
                    min_v = i

        if max_v - min_v <= 2:
            break

        count[arr[left]] -= 1
        left += 1

    answer = max(answer, right-left+1)

print(answer)