import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[1])

answer = 0
room = []
for i in range(n):
    if len(room) == 0:
        heapq.heappush(room, arr[i][2])
    else:
        while room:
            if room[0] > arr[i][1]:
                break
            else:
                heapq.heappop(room)
        heapq.heappush(room, arr[i][2])

    answer = max(answer, len(room))

print(answer)