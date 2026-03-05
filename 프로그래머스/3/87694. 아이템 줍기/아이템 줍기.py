from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
                
    grid = [[0] * (102) for _ in range(102)]
    
    for i in range(len(rectangle)):
        x1 = rectangle[i][0]
        y1 = rectangle[i][1]
        x2 = rectangle[i][2]
        y2 = rectangle[i][3]
        
        for x in range(x1 * 2, x2 * 2 + 1):
            for y in range(y1 * 2, y2 * 2 + 1):
                grid[x][y] = 1
    
    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]
    
    new_grid = [[0] * 102 for _ in range(102)]
    
    # 이동 경로 구현
    for x in range(102):
        for y in range(102):
            if grid[x][y] == 1:
                cnt = 0
                
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0 <= nx < 102 and 0 <= ny < 102:
                        if grid[nx][ny] == 1:
                            cnt += 1
                if cnt != 8:
                    new_grid[x][y] = 1
                        
    visited = [[-1] * 102 for _ in range(102)]
    
    que = deque()     
    que.append([characterX * 2, characterY * 2])
    visited[characterX * 2][characterY * 2] = 0
    
    while que:
        x, y = que.popleft()
        if x == itemX * 2 and y == itemY * 2:
            return visited[x][y] // 2
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < 102 and 0 <= ny < 102:
                if visited[nx][ny] == -1 and new_grid[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx, ny])
                    
    return new_grid
        