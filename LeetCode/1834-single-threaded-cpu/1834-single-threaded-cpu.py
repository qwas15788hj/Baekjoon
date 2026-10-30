from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        cpu, idle = [], []
        for i in range(len(tasks)):
            heappush(idle, [tasks[i][0], tasks[i][1], i])
        
        time = 0
        answer = []
        # answer 다 채울 때까지 진행
        while True:
            if len(answer) == len(tasks):
                break
            
            # 대기하는 idle에서 시작시간이 되면 cpu로 이동
            while idle:
                if idle[0][0] <= time:
                    start, work, idx = heappop(idle)
                    heappush(cpu, [work, idx])
                else:
                    break
            
            # cpu에 대기 중인 작업이 있다면, 작업 진행
            if cpu:
                work, idx = heappop(cpu)
                answer.append(idx)
                time += work
            # cpu에 대기 작업이 없으면, idle에서 가져오기
            else:
                start, work, idx = heappop(idle)
                heappush(cpu, [work, idx])
                time = start

        return answer
                