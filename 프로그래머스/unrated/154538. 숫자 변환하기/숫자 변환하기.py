from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue = deque() # 큐 생성
    visited = [False] * 1000001 # 방문처리 배열
    queue.append(x) # 첫 시작 선언
    visited[x] = True # 시작점 방문처리
    
    if visited[y] == True:
        return answer
    
    while queue: # 큐 반복
        size = len(queue) # 큐 길이
        for _ in range(size): # 큐 길이만큼 반복
            now = queue.popleft() # 큐 왼쪽 원소 빼기
            # 현재 요소 + n이 범위 안에 있고 방문 안했다면
            if 0 <= now + n <= y and not visited[now + n]:
                queue.append(now + n) # 큐에 삽입
                visited[now + n] = True # 방문 처리
            # 현재 요소 * 2이 범위 안에 있고 방문 안했다면
            if 0 <= now * 2 <= y and not visited[now * 2]:
                queue.append(now * 2) # 큐에 삽입
                visited[now * 2] = True # 방문 처리
            # 현재 요소 * 3이 범위 안에 있고 방문 안했다면
            if 0 <= now * 3 <= y and not visited[now * 3]:
                queue.append(now * 3) # 큐에 삽입
                visited[now * 3] = True # 방문 처리
            
        answer += 1 # 횟수 증가
        
        if visited[y] == True: # y가 방문 처리 됬다면 종료
            break
    
    if visited[y] == False: # y가 방문 처리 안됬다면 -1
        answer = -1
    
    return answer