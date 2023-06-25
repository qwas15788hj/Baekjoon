from collections import deque

def solution(n):
    answer = 0
    count = 0
    arr = deque()
    
    for i in range(1, n+1):
        count += i
        arr.append(i)
        if count == n:
            answer += 1
        elif count > n:
            while True:
                count -= arr.popleft()
                if count == n:
                    answer += 1
                elif count < n:
                    break
                    
    return answer