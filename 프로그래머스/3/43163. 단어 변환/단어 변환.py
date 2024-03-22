from collections import deque

def solution(begin, target, words):
    answer = 1e9
    
    visited = [False] * len(words)
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        now, count = queue.popleft()
        if now == target:
            answer = min(answer, count)
        
        for i in range(len(words)):
            cnt = 0
            for j in range(len(words[i])):
                if words[i][j] != now[j]:
                    cnt += 1
            
            if cnt == 1 and not visited[i]:
                queue.append([words[i], count+1])
                visited[i] = True
    
    if answer == 1e9:
        answer = 0
        
    return answer