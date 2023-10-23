import heapq

def solution(operations):
    arr = []
    
    for op in operations:
        if op.split()[0] == "I": # I 면 숫자 배열에 int형으로 저장
            heapq.heappush(arr, int(op.split()[1]))
        else:
            if len(arr): # 배열에 원소가 있고
                if op.split()[1] == "1": # D이면서 1이면 최댓값 삭제
                    arr.remove(max(arr))
                else: # D이면서 -1이면 최소값, 힙으로 제거
                    heapq.heappop(arr)
    
    if len(arr):
        return [max(arr), min(arr)]
    else:
        return [0, 0]