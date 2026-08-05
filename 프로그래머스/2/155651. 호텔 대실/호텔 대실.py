from heapq import heappush, heappop

def solution(book_time):
    answer = 0
    n = len(book_time)
    book_time.sort(key=lambda x:x[0])
    
    heap = []
    for i in range(n):
        s = int(book_time[i][0][:2])*60 + int(book_time[i][0][3:])
        e = int(book_time[i][1][:2])*60 + int(book_time[i][1][3:])
        if len(heap) == 0:
            heappush(heap, e)
        else:
            if heap[0]+10 <= s:
                heappop(heap)
                heappush(heap, e)
            else:
                heappush(heap, e)
        
        answer = max(answer, len(heap))
    
    return answer