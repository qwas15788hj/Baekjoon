def solution(a):
    answer = 0
    
    if len(a) <= 2:
        return len(a)
    else:
        right_arr = [a[-1]]
        for i in range(len(a)-2, -1, -1):
            right_arr.append(min(right_arr[-1], a[i]))
        right_arr.reverse()

        left = a[0]
        right = right_arr[2]
        for i in range(1, len(a)-1):
            left = min(left, a[i-1])
            right = right_arr[i+1]
            if a[i] < left or a[i] < right:
                answer += 1

        return answer + 2