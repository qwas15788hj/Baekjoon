import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

damage = []
for i in range(n):
    damage.append(9//3**i)
damage = list(permutations(damage, n))

queue = deque()
queue.append(arr)
if n ==1:
    visited = [False] * 61
elif n == 2:
    visited = [[False] * 61 for _ in range(61)]
elif n == 3:
    visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]

if n == 1:
    visited[arr[0]] = True
elif n == 2:
    visited[arr[0]][arr[1]] = True
elif n == 3:
    visited[arr[0]][arr[1]][arr[2]] = True

count = 0
flag = False
while queue:
    size = len(queue)
    for _ in range(size):
        scv = queue.popleft()
        if sum(scv) == 0:
            flag = True
            break
            
        for i in range(len(damage)):
            sub_scv = scv.copy()
            for j in range(len(damage[i])):
                sub_scv[j] = max(0, sub_scv[j]-damage[i][j])

            if n == 1:
                if not visited[sub_scv[0]]:
                    queue.append(sub_scv)
                    visited[sub_scv[0]] = True
            elif n == 2:
                if not visited[sub_scv[0]][sub_scv[1]]:
                    queue.append(sub_scv)
                    visited[sub_scv[0]][sub_scv[1]] = True
            elif n == 3:
                if not visited[sub_scv[0]][sub_scv[1]][sub_scv[2]]:
                    queue.append(sub_scv)
                    visited[sub_scv[0]][sub_scv[1]][sub_scv[2]] = True

    if flag:
        break
        
    count += 1
    
print(count)