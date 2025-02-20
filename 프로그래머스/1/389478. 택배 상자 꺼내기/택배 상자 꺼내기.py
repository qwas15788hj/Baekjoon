def solution(n, w, num):
    answer = 0
    
    arr = [[] for _ in range(w)]
    idx_odd, idx_even = 0, w-1
    for i in range(n):
        if (i//w)%2 == 0:
            arr[idx_odd%w].append(i+1)
            idx_odd += 1
        else:
            arr[idx_even].append(i+1)
            idx_even -= 1
            if idx_even == -1:
                idx_even = w-1
                
    for i in range(len(arr)):
        if num in arr[i]:
            answer = len(arr[i]) - arr[i].index(num)
            break
    
    return answer