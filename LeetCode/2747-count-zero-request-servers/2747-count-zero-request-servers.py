class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x:x[1])
        server, count, left, right = [0] * (n+1), 0, 0, 0

        queries_sub = []
        for i in range(len(queries)):
            queries_sub.append([queries[i], i])
        queries_sub.sort(key=lambda x:x[0])

        answer = [0] * len(queries)
        for q, i in queries_sub:
            while right < len(logs) and logs[right][1] <= q:
                if server[logs[right][0]] == 0:
                    count += 1
                server[logs[right][0]] += 1
                right += 1

            while left < len(logs) and logs[left][1] < q-x:
                server[logs[left][0]] -= 1
                if server[logs[left][0]] == 0:
                    count -= 1
                left += 1
            
            answer[i] = n-count

        return answer