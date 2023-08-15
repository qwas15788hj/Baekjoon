import heapq

def solution(book_time):
    answer = 0
    
    # 입실, 퇴실 시간 분으로 변경
    for book in book_time:
        book[0] = int(book[0][0] + book[0][1]) * 60 + int(book[0][3] + book[0][4])
        book[1] = int(book[1][0] + book[1][1]) * 60 + int(book[1][3] + book[1][4])
        
    # 입실 시간 기준으로 오름차순 정렬
    book_time.sort(key=lambda x:x[0])
    
    # 방 배정 (우선순위 큐, 힙 사용)
    arr = []
    for book in book_time: # 모든 방 탐색
        if len(arr) == 0: # 사용 중인 방이 없다면
            heapq.heappush(arr, book[1]) # 퇴실 시간 넣기
        else: # 사용 중인 방이 있다면
            if arr[0] + 10 <= book[0]: # 입실 시간이 가장 빠른 퇴실 시간 + 10분보다 크거나 같으면 해당 방 사용 가능
                heapq.heappop(arr) # 해당 방 빼고
                heapq.heappush(arr, book[1]) # 현재 입실하는 사람의 퇴실 시간 넣기
            else: # 입실 시간이 퇴실 시간 + 10분보다 작으면
                heapq.heappush(arr, book[1]) # 새로운 방 사용
    
    return len(arr) # 사용 중인 방 return