from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # 각 수가 위치한 인덱스 저장
        dic = dict()
        for i in range(n):
            if arr[i] not in dic:
                dic[arr[i]] = [i]
            else:
                dic[arr[i]].append(i)
        
        answer = 0
        flag = False
        queue = deque([])
        visited = [False] * n
        queue.append(0)
        visited[0] = True
        while queue:
            size = len(queue)
            for _ in range(size):
                x = queue.popleft()
                if x == n-1:
                    flag = True
                    break

                # 인덱스-1 체크
                if 0 <= x-1 and not visited[x-1]:
                    queue.append(x-1)
                    visited[x-1] = True
                # 인덱스+1 체크
                if x+1 < n and not visited[x+1]:
                    queue.append(x+1)
                    visited[x+1] = True
                # 해당 수를 방문안했다면, 같은 수의 모든 위치 체크
                # 시간초과를 위해 확인한 수 dic 삭제
                if arr[x] in dic:
                    for nx in dic[arr[x]]:
                        if not visited[nx]:
                            queue.append(nx)
                            visited[nx] = True
                    del dic[arr[x]]
                
            if flag:
                break
            
            answer += 1
        
        return answer