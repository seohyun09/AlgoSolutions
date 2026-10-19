from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1
    
    que = deque()
    que.append([0, 0])
    
    while que:
        x, y = que.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 방문하지 않은 경우
            if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx, ny]) 

    return visited[n-1][m-1]
