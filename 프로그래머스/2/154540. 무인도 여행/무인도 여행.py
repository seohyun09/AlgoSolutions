from collections import deque

def solution(maps):
    
    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    MAPS = [[-1] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                MAPS[i][j] = int(maps[i][j])
    # print(MAPS)
    
    visited = [[False] * m for _ in range(n)]
    
    def bfs(si, sj):
        
        que = deque()
        que.append([si, sj])
        visited[si][sj] = True
        
        total = MAPS[si][sj]
        
        while que:
            
            i, j = que.popleft()
            
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                
                if not visited[ni][nj] and MAPS[ni][nj] != -1:
                    que.append([ni, nj])
                    visited[ni][nj] = True
                    total += MAPS[ni][nj]
        
        return total
    
    answer = []
    
    for i in range(n):
        for j in range(m):
            if MAPS[i][j] != -1 and not visited[i][j]:
                val = bfs(i, j)
                answer.append(val)

    if len(answer) > 0:
        return sorted(answer)
    
    return [-1]