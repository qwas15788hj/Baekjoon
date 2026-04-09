n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[[] for _ in range(n)] for _ in range(n)]
piece = []
for i in range(k):
    a, b, c = map(int, input().split())
    piece.append([a-1, b-1, c-1])
    visited[a-1][b-1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def check(a, b):
    if len(visited[a][b]) >= 4:
        return True
    return False

answer = 1
flag = False
# 1000번 이하만 돌리기
for _ in range(1000):
    # 한 턴 시작
    for i in range(k):
        x, y, d = piece[i]
        # 다음 위치
        nx = x + dx[d]
        ny = y + dy[d]

        # for v in visited:
        #     print(v)
        # print(piece)
    
        # 이동X, 이동하는 말
        idx = visited[x][y].index(i)
        no_move = visited[x][y][:idx]
        move = visited[x][y][idx:]
        # print(move)
        # print("====")
        
        # 다음 이동하려는 칸이 흰색인 경우
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            visited[x][y] = no_move
            visited[nx][ny] += move
            for m in move:
                piece[m][0] = nx
                piece[m][1] = ny
            if check(nx, ny):
                flag = True
                break
                
        # 다음 이동하려는 칸이 빨간색일 경우
        elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            visited[x][y] = no_move
            visited[nx][ny] += move[::-1]
            for m in move:
                piece[m][0] = nx
                piece[m][1] = ny
            if check(nx, ny):
                flag = True
                break
                
        # 다음 이동하려는 칸이 파랑색이거나, 벗어나는 경우
        else:
            # 방향을 반대로 변경
            if d%2 != 0:
                d -= 1
            else:
                d += 1
            piece[i] = [x, y, d]
            
            nx = x + dx[d]
            ny = y + dy[d]
            # 다음 이동하려는 칸이 흰색인 경우
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                visited[x][y] = no_move
                visited[nx][ny] += move
                for m in move:
                    piece[m][0] = nx
                    piece[m][1] = ny
                if check(nx, ny):
                    flag = True
                    break
                
            # 다음 이동하려는 칸이 빨간색일 경우
            elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                visited[x][y] = no_move
                visited[nx][ny] += move[::-1]
                for m in move:
                    piece[m][0] = nx
                    piece[m][1] = ny
                if check(nx, ny):
                    flag = True
                    break

        if flag:
            break
            
    if flag:
        break
        
    answer += 1

if answer > 1000:
    print(-1)
else:
    print(answer)
        