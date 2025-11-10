import sys
from collections import deque
n, m=map(int, sys.stdin.readline().split())

maze=[]
for _ in range(n):
  line=list(map(int, sys.stdin.readline().rstrip()))
  maze.append(line)

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

que=deque()
que.append((0, 0))

while que:
  x, y=que.popleft()

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>=0 and ny>=0 and nx<m and ny<n and maze[ny][nx]==1:
      que.append((nx, ny))
      maze[ny][nx]=maze[y][x]+1
    
print(maze[n-1][m-1])