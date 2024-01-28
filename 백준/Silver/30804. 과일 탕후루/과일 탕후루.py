n = int(input())
arr = list(map(int, input().split()))
left, right = 0, 0
count, answer = 0, 0
dic = dict()

while right < n:
    if count < 2:
        if arr[right] not in dic:
            dic[arr[right]] = 1
            count += 1
        else:
            dic[arr[right]] += 1

    elif count == 2 and arr[right] in dic:
        dic[arr[right]] += 1

    elif count == 2 and arr[right] not in dic:
        while count != 1:
            if dic[arr[left]] == 1:
                del dic[arr[left]]
                count -= 1
            else:
                dic[arr[left]] -= 1
            left += 1

        dic[arr[right]] = 1
        count += 1

    answer = max(answer, right - left + 1)
    right += 1

print(answer)