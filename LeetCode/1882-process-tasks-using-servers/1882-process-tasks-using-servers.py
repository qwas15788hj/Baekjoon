from heapq import heappush, heappop

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        work, wait = [], []
        for i in range(len(servers)):
            heappush(wait, [servers[i], i])
        
        answer = [0] * len(tasks)
        for i in range(len(tasks)):
            # 현재 시간보다 끝나는 시간이 빠르면 work 종료시키고 wait로 이동
            while work:
                if work[0][0] <= i:
                    time, weight, idx = heappop(work)
                    heappush(wait, [weight, idx])
                else:
                    break

            # 쉬고 있는 서버 있다면, 쉬는 서버 꺼내서 일 중인 서버 work에 [종료시간, 가중치, 인덱스] 저장
            if wait:
                weight, idx = heappop(wait)
                heappush(work, [i+tasks[i], weight, idx])
                answer[i] = idx
            # 쉬고 있는 서버 없다면, 일하는 서버 work에서 꺼내기
            else:
                time, weight, idx = heappop(work)
                heappush(work, [time+tasks[i], weight, idx])
                answer[i] = idx
        
        return answer