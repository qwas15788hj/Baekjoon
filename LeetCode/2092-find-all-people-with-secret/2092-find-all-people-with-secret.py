from heapq import heappush, heappop
from collections import deque

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        heap = []
        for x, y, time in meetings:
            heappush(heap, [time, x, y])

        visited = [False] * n
        visited[0], visited[firstPerson] = True, True
        while heap:
            time, x, y = heappop(heap)
            dic = dict()
            dic[x], dic[y] = [y], [x]
            while heap:
                if heap[0][0] == time:
                    t, x, y = heappop(heap)
                    if x in dic:
                        dic[x].append(y)
                    else:
                        dic[x] = [y]

                    if y in dic:
                        dic[y].append(x)
                    else:
                        dic[y] = [x]
                else:
                    break
            
            queue = deque([])
            for key, value in dic.items():
                if visited[key]:
                    queue.append(key)
            
            while queue:
                x = queue.popleft()
                for nx in dic[x]:
                    if not visited[nx]:
                        queue.append(nx)
                        visited[nx] = True
        
        answer = []
        for i in range(n):
            if visited[i]:
                answer.append(i)

        return answer